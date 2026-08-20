---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_TextEntryCollectionViewCell_swift.html
archived_at: '2026-07-15T04:56:07.080687Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-CascadingLayout.swift.md)[Previous](LucidDreams-MultiPaneLayout.swift.md)

# LucidDreams/TextEntryCollectionViewCell.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Defines a simple collection view cell that allows for text entry.
*/

import UIKit

/// A collection view cell that displays a text field.
class TextEntryCollectionViewCell: UICollectionViewCell {
    // MARK: Properties

    static let reuseIdentifier = "\(TextEntryCollectionViewCell.self)"

    @IBOutlet var textField: UITextField!

    // MARK: Life Cycle

    override func awakeFromNib() {
        textField.addTarget(textField, action: #selector(UITextField.resignFirstResponder), for: .editingDidEndOnExit)
    }
}
```

[Next](LucidDreams-CascadingLayout.swift.md)[Previous](LucidDreams-MultiPaneLayout.swift.md)

