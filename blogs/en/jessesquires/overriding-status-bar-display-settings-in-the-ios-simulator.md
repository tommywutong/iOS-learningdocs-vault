---
title: Overriding status bar display settings in the iOS simulator
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2019/09/26/overriding-status-bar-settings-ios-simulator/'
original_language: en
published: 2019-09-26
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:235743d81b50a3f3'
translated: false
---

> 原文：[Overriding status bar display settings in the iOS simulator](https://www.jessesquires.com/blog/2019/09/26/overriding-status-bar-settings-ios-simulator/)　·　Jesse Squires

With [version 11 of Xcode](https://developer.apple.com/documentation/xcode_release_notes/xcode_11_release_notes), the IDE ships with a new feature in the `simctl` tool that can override status bar values for iOS simulators. This allows you to [take better screenshots](https://www.jessesquires.com/blog/2014/08/03/status-bars-matter/) for the App Store without having to worrying about the time, battery level, etc. It is a great improvement, but there are some significant shortcomings. I’ve written a script to fix at least some of those.

##### In This Series

This post is part of a series about overriding status bar display settings in the iOS simulator.

1. Overriding status bar display settings in the iOS simulator
2. [A script to automate overriding iOS simulator status bar values](https://www.jessesquires.com/blog/2019/09/30/automating-simctl-status-bar/)
3. [Fully automating perfect status bar overrides for iOS simulators with Nine41](https://www.jessesquires.com/blog/2020/04/13/fully-automating-perfect-status-bar-overrides-for-ios-simulators/)
4. [Workaround: simctl status_bar broken for iOS 16 simulators](https://www.jessesquires.com/blog/2022/12/14/simctrl-status_bar-broken/)
5. [Workaround: Xcode simctl status_bar is still broken for iOS 17 simulators](https://www.jessesquires.com/blog/2024/01/04/simctl-status_bar-still-broken/)

Before Xcode 11, developers needed to rely on third-party tools like Dave Verwer’s [SimulatorStatusMagic](https://github.com/shinydevelopment/SimulatorStatusMagic) (now deprecated in favor of `simctl status_bar`). It is convenient to see this become a first-party tool instead.

### Using `simctl status_bar`

To begin using this feature, run `xcrun simctl status_bar` in your terminal, which will print a usage explanation and the list of possible override options. Here’s an example for a simulator named “iPhone 11”:

```
$ xcrun simctl status_bar "iPhone 11" override --time 9:41 --dataNetwork wifi --wifiMode active --wifiBars 3 --cellularMode active --cellularBars 4 --batteryState charged --batteryLevel 100
```

This produces the following:

![iOS status bar](https://www.jessesquires.com/img/blog/simctl-status-bar.png)

You can specify the time, WiFi state, cellular state, and battery state. What’s really nice is that you can specify the simulator using only its name, not some obscure identifier. If you hover your mouse over a simulator device, or bring its window to the front, it will display its name and OS version beneath it. Or, if you have “Show Device Bezels” turned off, the name and OS version will display in the window’s title bar.

The overrides in this example are the ones I plan to use for all of my screenshots, and I recommend you do the same — full cellular bars, full WiFi bars, full battery, and 9:41 for the time. This is what Apple uses for all of their marketing screenshots, and there is no doubt that it is intentional. The time 9:41 is strangely aesthetically pleasing, and I’m sure someone spent a lot of time to figure that out. **Update:** Or, [perhaps not](https://www.engadget.com/2014/04/14/why-9-41-am-is-the-always-the-time-displayed-on-iphones-and-ipad/). 😄

### Shortcomings

The most frustrating issue is that any status bar overrides that you set **do not persist** across simulator launches. If you close (shutdown) a simulator and relaunch it, the status bar returns to its default state. This means you end up running the above command often, which is difficult to remember at 181 characters.

However, you can create a custom bash command so you don’t have to remember. You can add the following to your `~/.bash_profile`:

```
function fix_status_bar() {
    ( set -x; xcrun simctl status_bar "$1" override --time 9:41 --dataNetwork wifi --wifiMode active --wifiBars 3 --cellularMode active --cellularBars 4 --batteryState charged --batteryLevel 100 )
}
```

And then run the command:

```
$ fix_status_bar "iPhone 11"
```

This is much more usable. Note: using `set -x;` and wrapping the command in `( )` (creating a subshell) will echo the command to your terminal, so you can see exactly what is being executed. You can remove these if you like.

One nice-to-have would be to make these overrides the defaults such that you could run `xcrun simctl status_bar "<DEVICE>" override` without specifying any options to get “Apple Marketing approved” status bars.

Another aspect of the simulator status bars on “notch-less” iPhones (iPhones before the X) is that they display “Carrier” for the cellular carrier. I do not think `simctl status_bar` should let you override this with a custom value, since cellular carriers are not the same in all locales. However, I think you should be able to **remove** this. ~~You cannot. But, I suppose most folks are going to be taking screenshots using the latest devices, which means this should not be much of a concern.~~

##### [Update](#updated-28-september-2019)  _28 September 2019_

Some readers have pointed out that you _can_ remove the “Carrier” text by specifying `--cellularMode notSupported`. However, this has the unfortunate side-effect of also removing the cellular bars. Also, currently the App Store requires that you provide two sets of screenshots, one for “notched” iPhones (e.g. iPhone XS Max) and one for “notch-less” (e.g. iPhone 8 Plus). One reader noted a recent experience of getting rejected for using iPhone X screenshots for the iPhone Plus. It appears this shortcoming is worse than I initially anticipated.

Finally, I think all of these options should be present in the Simulator.app File menu, which already includes options like showing the in-call status bar and setting a custom location.

It would be nice to see these improvements in future releases: default override values, persistence of these settings across launches, and a way to toggle the defaults from the simulator app.
