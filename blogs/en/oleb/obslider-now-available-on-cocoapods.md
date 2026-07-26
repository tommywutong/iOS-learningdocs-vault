---
title: OBSlider Now Available on CocoaPods
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/06/obslider-now-available-on-cocoapods/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:4786581e603d8cb2'
translated: false
---

> 原文：[OBSlider Now Available on CocoaPods](https://oleb.net/blog/2012/06/obslider-now-available-on-cocoapods/)　·　Ole Begemann

# OBSlider Now Available on CocoaPods

[`OBSlider`](https://github.com/ole/OBSlider), my `UISlider` subclass that adds variable scrubbing speeds (just like in the Music app on iOS), is now also available via the [CocoaPods](http://cocoapods.org) library manager. CocoaPods makes handling open-source libraries that you use in your Xcode projects much easier than configuring your projects manually.

# Using CocoaPods

## Installation

If you haven’t installed CocoaPods yet, do so first:

```
> gem install cocoapods
> pod setup
```

Use `sudo gem install cocoapods` if the command fails without `sudo`.

## Write a Podfile for Your Project

Next, you need to add a `Podfile` to your project folder. The Podfile is a simple text file that lists all the third-party components you want to use in your project. Go to the folder where your project is located and add it (I’m using Textmate here but use any text editor you like):

```
> mate Podfile
platform :ios
dependency 'OBSlider'
```

## Install the Dependencies and Configure Your Project

Now you can install the dependencies with one call:

```
> pod install MyApp.xcodeproj
```

This command will create a `Pods` subfolder and download all pods from their repositories on GitHub. CocoaPods will also create a new `MyApp.xcworkspace` that you should use to open your project in Xcode from now on. The newly created workspace combines your own project and a separate CocoaPods project that builds all third-party libraries for you and links them into your own code.

One cool thing about CocoaPods is that it knows which libraries use [ARC](http://clang.llvm.org/docs/AutomaticReferenceCounting.html) and which don’t. It will automatically add the correct compiler flags to each file, which makes it super easy to mix ARC and non-ARC code.

If you later add more dependencies to your Podfile, you don’t have to specify your project anymore. A simple `pod install` command is enough to add them. The [CocoaPods Wiki](https://github.com/CocoaPods/CocoaPods/wiki) has more info on the available commands.

# Add Your Own Components to CocoaPods

If you have your own open-source libraries for iOS or OS X, you may want to consider making them available through CocoaPods, too. Doing so is very easy.

## Writing a Podspec

First, you need to write a so-called podspec for your library. The podspec is a short file containing Ruby code that gives CocoaPods some metadata about your library and tells it where it can get the code (usually from GitHub). As an example, this is `OBSlider.podspec`:

```
Pod::Spec.new do |s|
  s.name     = 'OBSlider'
  s.version  = '1.1.0'
  s.license  = 'MIT'
  s.summary  = 'A UISlider subclass that adds variable scrubbing speeds.'
  s.homepage = 'https://github.com/ole/OBSlider'
  s.author   = { 'Ole Begemann' => 'ole@oleb.net' }
  s.source   = { :git => 'https://github.com/ole/OBSlider.git', :tag => '1.1.0' }
  s.description = 'OBSlider is a UISlider subclass that adds variable scrubbing speeds as seen in the Music app on iOS. While scrubbing the slider, the user can slow down the scrubbing speed by moving the finger up or down (away from the slider). The distance thresholds and slowdown factors can be freely configured by the developer.'
  s.platform = :ios
  s.source_files = 'OBSlider/**/*.{h,m}'
  s.clean_paths = "OBSliderDemo"
  s.requires_arc = true
end
```

Most of the spec should be self-explanatory, especially since the `pod spec create MyLibrary` command creates a well-commented sample file that you can base your own on.

When you have created your spec and it passes the validation (`pod spec lint MyLibrary.podspec`), you should add it to the official [CocoaPods Specs repository](https://github.com/CocoaPods/Specs). You can do that by forking the repo on GitHub and adding your podspec to it in a `MyLibrary/x.x.x` folder where `x.x.x` is the version number of your library. Then create a pull request to make the CocoaPods guys aware of your spec.

# Migrated OBSlider to ARC

In the process of adding `OBSlider` to CocoaPods, I also migrated the code to ARC and modernized the code base a little bit (for example, by relying on the compiler to synthesize ivars for properties). The new code runs on iOS 5.0+ only and really, there’s [no need to require iOS 4](http://www.ilounge.com/index.php/news/comments/ios-update-365-million-devices-80-running-ios-5/) anymore. If you still do, the old code is still available as version 1.0.0 (tagged [1.0.0](https://github.com/ole/OBSlider/commit/a7b5187a84c8d5a02549b1cb352926cee93a9f2e) on GitHub) while the ARCified version is [1.1.0](https://github.com/ole/OBSlider/commit/f3d22a09880f6c7b34dc5619ca427c8276bb3167).

To use version 1.0.0 with CocoaPods, specify the version number in your Podfile:

```
dependency 'OBSlider', '1.0.0'
```
