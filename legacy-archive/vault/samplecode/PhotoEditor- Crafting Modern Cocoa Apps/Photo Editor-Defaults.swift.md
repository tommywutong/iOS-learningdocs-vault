---
title: 'PhotoEditor: Crafting Modern Cocoa Apps'
apple_id: TP40017384
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoEditor/Listings/Photo_Editor_Defaults_swift.html
archived_at: '2026-07-18T03:18:49.147677Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoEditor: Crafting Modern Cocoa Apps](PhotoEditor-%20Crafting%20Modern%20Cocoa%20Apps.md)


[Next](Photo%20Editor-EffectsAccessoryViewController.swift.md)[Previous](Photo%20Editor-CanvasView.swift.md)

# Photo Editor/Defaults.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Defaults is a nice wrapper around NSUserDefaults and declares our global user defaults (useDarkMode)
 */

import Cocoa

struct PreferenceKey<Value> : RawRepresentable {
    typealias RawValue = String 
    let rawValue: RawValue

    init (_ key: String) {
        rawValue = key
    }

    // Appease the protocol.
    init (rawValue: RawValue) {
        self.rawValue = rawValue
    }

}

extension Notification.Name {
    static let appearanceChanged = Notification.Name(rawValue: "AppearanceChangedNotification")
}

extension UserDefaults {
    subscript(key: PreferenceKey<Bool>) -> Bool {
        set { set(newValue, forKey: key.rawValue) }
        get { return bool(forKey: key.rawValue) }
    }

    subscript(key: PreferenceKey<Float>) -> Float {
        set { set(newValue, forKey: key.rawValue) }
        get { return float(forKey: key.rawValue) }
    }

    subscript(key: PreferenceKey<Double>) -> Double {
        set { set(newValue, forKey: key.rawValue) }
        get { return double(forKey: key.rawValue) }
    }

    subscript(key: PreferenceKey<Int>) -> Int {
        set { set(newValue, forKey: key.rawValue) }
        get { return integer(forKey: key.rawValue) }
    }
}

// User defaults for our application
extension UserDefaults {
    static let useDarkModeKey = PreferenceKey<Bool>("UseDarkMode")

    static var useDarkMode: Bool {
        get {
            return UserDefaults.standard[useDarkModeKey]
        }
    }
}
```

[Next](Photo%20Editor-EffectsAccessoryViewController.swift.md)[Previous](Photo%20Editor-CanvasView.swift.md)

