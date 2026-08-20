---
title: 'MyLife: A simple app for starting iOS development'
apple_id: TP40017272
resource_type: Sample Code
platform: iOS
topic: General
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/MyLife/Listings/MyLife_Person_swift.html
archived_at: '2026-07-18T03:16:38.238561Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyLife: A simple app for starting iOS development](MyLife-%20A%20simple%20app%20for%20starting%20iOS%20development.md)


[Next](MyLife-PeopleTableViewController.swift.md)[Previous](MyLife-AppDelegate.swift.md)

# MyLife/Person.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A Person class contains the data to that is stored for each person displayed in the app.

    Customizations: Whenever you want to add new data about a Person, you will need to create new variables here to store that data. To learn more you can check out the the README file included in the app.
*/

import UIKit

/// This class defines the data that is stored for each person.
class Person {    
    // MARK: Properties

    var name: String?

    var image: UIImage?

    /// How much do they like dogs on a scale from 0 to 10.
    var dogPreference: Float?

    // MARK: Initialization

    init(name: String? = nil, image: UIImage? = nil, dogPreference: Float? = nil) {
        self.name = name
        self.image = image
        self.dogPreference = dogPreference
    }
}
```

[Next](MyLife-PeopleTableViewController.swift.md)[Previous](MyLife-AppDelegate.swift.md)

