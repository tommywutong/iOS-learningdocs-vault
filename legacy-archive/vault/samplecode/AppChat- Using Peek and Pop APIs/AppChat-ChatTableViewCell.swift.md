---
title: 'AppChat: Using Peek and Pop APIs'
apple_id: TP40017298
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/AppChat/Listings/AppChat_ChatTableViewCell_swift.html
archived_at: '2026-07-18T03:01:06.186481Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AppChat: Using Peek and Pop APIs](AppChat-%20Using%20Peek%20and%20Pop%20APIs.md)


[Next](AppChat-NewChatDelegate.swift.md)[Previous](AppChat-ChatReplyPresentAnimator.swift.md)

# AppChat/ChatTableViewCell.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The table view cell class used to display a received chat.
 */

import UIKit

class ChatTableViewCell: UITableViewCell {
    static let identifier = "ChatTableViewCell"

    override init(style: UITableViewCellStyle, reuseIdentifier: String?) {
        super.init(style: .subtitle, reuseIdentifier: reuseIdentifier)
    }

    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
    }

    override func layoutSubviews() {
        super.layoutSubviews()

        if let imageView = imageView {
            imageView.contentMode = .scaleAspectFit
            imageView.clipsToBounds = true
            let imageSize = 0.9 * contentView.bounds.height
            var bounds = imageView.bounds
            bounds.size.width = imageSize
            bounds.size.height = imageSize
            imageView.bounds = bounds
            imageView.layer.cornerRadius = imageSize / 2.0
        }
    }

    func accessoryType(for chatItem: ChatItem) -> UITableViewCellAccessoryType {
        if chatItem.saved {
            return .checkmark
        }
        else {
            return .none
        }
    }

    func configure(with chatItem: ChatItem) {
        imageView?.image = chatItem.sender.profilePhoto
        accessoryType = accessoryType(for: chatItem)
        let format = NSLocalizedString("Chat from %@", comment: "Format string for a chat received from a friend")
        textLabel?.text = String(format: format, chatItem.sender.name)
        detailTextLabel?.text = chatItem.date.timeAgoString()
    }
}
```

[Next](AppChat-NewChatDelegate.swift.md)[Previous](AppChat-ChatReplyPresentAnimator.swift.md)

