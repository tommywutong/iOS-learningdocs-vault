---
title: 'UnicornChat: Extending Your Apps with SiriKit'
apple_id: TP40017332
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/UnicornChat/Listings/UnicornCore_UCChatView_m.html
archived_at: '2026-07-18T03:27:33.523335Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnicornChat: Extending Your Apps with SiriKit](UnicornChat-%20Extending%20Your%20Apps%20with%20SiriKit.md)


[Next](UnicornCore-UCAddressBookManager.m.md)[Previous](UnicornCore-UCContact.m.md)

# UnicornCore/UCChatView.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The view that displays messages in UnicornChat.
*/

#import "UCChatView.h"

@implementation UCChatView {
    UILabel *_recipientLabel;
    UILabel *_contentLabel;
    UIImageView *_mockView;

    UIImage *_draftMock;
    UIImage *_sentMock;
}

- (instancetype)initWithFrame:(CGRect)frame {
    self = [super initWithFrame:frame];
    if (self) {
        _draftMock = [UIImage imageNamed:@"chatmockdraft.png"];
        _sentMock = [UIImage imageNamed:@"chatmock.png"];

        _mockView = [[UIImageView alloc] initWithImage:_draftMock];
        [_mockView setContentMode:UIViewContentModeScaleToFill];
        [self addSubview:_mockView];

        _recipientLabel = [[UILabel alloc] init];
        [_recipientLabel setNumberOfLines:0];
        [_recipientLabel setLineBreakMode:NSLineBreakByWordWrapping];
        [_recipientLabel setTextColor:[UIColor whiteColor]];
        [self addSubview:_recipientLabel];

        _contentLabel = [[UILabel alloc] init];
        [_contentLabel setNumberOfLines:0];
        [_contentLabel setLineBreakMode:NSLineBreakByWordWrapping];
        [self addSubview:_contentLabel];
    }
    return self;
}

- (void)layoutSubviews {
    [super layoutSubviews];

    [_mockView setFrame:[self bounds]];

    [_recipientLabel setText:_recipientName];
    [_recipientLabel setFrame:CGRectMake(65.0, 22.0, 62.0, 30.0)];

    [_contentLabel setText:_content];
    [_contentLabel setFrame:CGRectMake(113.0, 85.0, 150.0, 75.0)];
}

- (void)setSent:(BOOL)sent {
    if (_sent == sent) {
        return;
    }

    _sent = sent;

    UIImage *mockImage = (_sent ? _sentMock : _draftMock);
    [_mockView setImage:mockImage];
}

- (void)setContent:(NSString *)content {
    if ([_content isEqualToString:content]) {
        return;
    }
    _content = content;

    [self setNeedsLayout];
}

- (void)setRecipientName:(NSString *)recipientName {
    if ([_recipientName isEqualToString:recipientName]) {
        return;
    }
    _recipientName = recipientName;

    [self setNeedsLayout];
}

@end
```

[Next](UnicornCore-UCAddressBookManager.m.md)[Previous](UnicornCore-UCContact.m.md)

