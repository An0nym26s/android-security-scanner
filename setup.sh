#!/bin/bash

# This script installs the Android SDK and necessary dependencies.

# Update and install required packages
sudo apt update
sudo apt install -y openjdk-11-jdk wget

# Set environment variables
ANDROID_SDK_URL=https://dl.google.com/android/repository/commandlinetools-linux-7583922_latest.zip
ANDROID_SDK_DIR=$HOME/Android/Sdk

# Create SDK directory
mkdir -p $ANDROID_SDK_DIR

# Download and extract the Android SDK command line tools
cd $ANDROID_SDK_DIR
wget $ANDROID_SDK_URL
unzip commandlinetools-linux-7583922_latest.zip
rm commandlinetools-linux-7583922_latest.zip

# Install SDK components using the command line tools
echo 'y' | sdkmanager --sdk_root=$ANDROID_SDK_DIR --install "platform-tools" "platforms;android-30"