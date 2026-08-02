---
title: StitchedStreamPlayer
apple_id: DTS40010092
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-07-14'
source_url: https://developer.apple.com/library/archive/samplecode/StitchedStreamPlayer/Listings/Classes_MyStreamingMovieViewController_h.html
archived_at: '2026-07-18T03:25:45.705770Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [StitchedStreamPlayer](StitchedStreamPlayer.md)


[Next](Classes-MyPlayerLayerView.h.md)[Previous](main.m.md)

# Classes/MyStreamingMovieViewController.h

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
A UIViewController controller subclass that loads the SecondView nib file that contains its view.
 Contains an action method that is called when the Play Movie button is pressed to play the movie.
 Provides a text edit control for the user to enter a movie URL.
 Manages a collection of transport control UI that allows the user to play/pause and seek.
*/

@import UIKit;
@import AVFoundation;
@import CoreMedia;

@class AVPlayer;
@class AVPlayerItem;
@class MyPlayerLayerView;

@interface MyStreamingMovieViewController : UIViewController <UITextFieldDelegate> {

    NSURL *movieURL;
    AVPlayer *player;
    AVPlayerItem *playerItem;
    MyPlayerLayerView *playerLayerView;

    UITextField *movieURLTextField;

    UISlider *movieTimeControl;
    BOOL isSeeking;
    BOOL seekToZeroBeforePlay;
    float restoreAfterScrubbingRate;

    id timeObserver;    

    UIToolbar *toolBar;
    UIBarButtonItem *playButton;
    UIBarButtonItem *stopButton;

    UILabel *isPlayingAdText;

    NSArray *adList;

}

@property (retain) IBOutlet UIToolbar *toolBar;
@property (retain) IBOutlet UIBarButtonItem *playButton;
@property (retain) IBOutlet UIBarButtonItem *stopButton;

@property (retain) IBOutlet UITextField *movieURLTextField;
@property (retain) IBOutlet UISlider *movieTimeControl;
@property (retain) IBOutlet MyPlayerLayerView *playerLayerView;
@property (retain) AVPlayer *player;
@property (retain) AVPlayerItem *playerItem;
@property (retain) IBOutlet UILabel *isPlayingAdText;

- (IBAction)loadMovieButtonPressed:(id)sender;

- (IBAction)beginScrubbing:(id)sender;
- (IBAction)scrub:(id)sender;
- (IBAction)endScrubbing:(id)sender;

- (IBAction)play:(id)sender;
- (IBAction)pause:(id)sender;

@end
```

[Next](Classes-MyPlayerLayerView.h.md)[Previous](main.m.md)

