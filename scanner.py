import subprocess
import time

class AndroidSecurityScanner:
    def __init__(self):
        self.adb_path = 'adb'

    def execute_adb_command(self, command):
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            print(f'Error executing command: {command}\n{e.stderr.decode('utf-8')}')
            return None

    def check_permissions(self, package_name):
        command = f'{self.adb_path} shell dumpsys package {package_name}'
        output = self.execute_adb_command(command)
        if output:
            permissions = self.parse_permissions(output)
            return permissions
        return None

    def parse_permissions(self, output):
        permissions = []
        lines = output.split('\n')
        for line in lines:
            if 'permission=' in line:
                perm = line.split('=')[1].strip()
                permissions.append(perm)
        return permissions

    def scan_device(self):
        print('Scanning for installed packages...')
        packages = self.execute_adb_command(f'{self.adb_path} shell pm list packages')
        if packages:
            package_list = packages.split('\n')
            for pkg in package_list:
                pkg_name = pkg.replace('package:', '')
                print(f'Checking permissions for {pkg_name}...')
                permissions = self.check_permissions(pkg_name)
                if permissions:
                    print(f'Permissions for {pkg_name}: {permissions}')
                else:
                    print(f'No permissions found for {pkg_name}.')

    def run(self):
        retries = 3
        for attempt in range(retries):
            try:
                self.scan_device()
                break  # Exit loop if successful
            except Exception as e:
                print(f'Attempt {attempt + 1} failed: {e}')
                time.sleep(2)  # wait before retrying
        else:
            print('All attempts failed. Please check your ADB connection and permissions.')

if __name__ == '__main__':
    scanner = AndroidSecurityScanner()
    scanner.run()