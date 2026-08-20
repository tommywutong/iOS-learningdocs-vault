---
title: iPod Library Access Programming Guide
apple_id: TP40008765
resource_type: Guide
platform: tvOS|iOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Audio/Conceptual/iPodLibraryAccess_Guide/UsingtheMediaItemPicker/UsingtheMediaItemPicker.html
archived_at: '2026-07-15T05:20:54.193904Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iPod Library Access Programming Guide](Introduction.md)


[Next](Using%20the%20iPod%20Library.md)[Previous](Using%20Media%20Playback.md)

# Using the Media Item Picker

The media item picker is the pre-packaged view controller for letting a user choose media items from the device iPod library. Using the picker is very simple:

1. Designate a [controller object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) as a [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) of the picker.
2. Invoke the picker from the controller.
3. When the user indicates that they are finished, the delegate receives the chosen collection of media items and dismisses the picker.

To set up a controller object as a media item picker delegate, first add the protocol’s name in the interface declaration in the controller’s header file, as follows:

```objc
@interface myController : UIViewController <MPMediaPickerControllerDelegate> {
    // interface declaration
}
```

Next, implement the two delegate methods from that protocol. The first method, shown in Listing 3-1, responds to the user having chosen some media items. It dismisses the picker and invokes the controller’s playback queue update method.

__Listing 3-1__  Responding to a new collection of media items from the picker

```objc
- (void) mediaPicker: (MPMediaPickerController *) mediaPicker
            didPickMediaItems: (MPMediaItemCollection *) collection {

    [self dismissModalViewControllerAnimated: YES];
    [self updatePlayerQueueWithMediaCollection: collection];
}
```

For example code showing how to update a playback queue, see [Listing 2-5](Using%20Media%20Playback.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donrvfvbuqmjqgawvgvzw).

The second picker delegate method handles the case of the user tapping Done without having chosen any items to play. See Listing 3-2 for a basic implementation.

__Listing 3-2__  Responding if the user cancels the picker

```objc
- (void) mediaPickerDidCancel: (MPMediaPickerController *) mediaPicker {

    [self dismissModalViewControllerAnimated: YES];
}
```


Listing 3-3 shows how to configure and display a media item picker—including establishing the controller object as the delegate of the picker.

__Listing 3-3__  Displaying a media item picker

```
MPMediaPickerController *picker =
    [[MPMediaPickerController alloc]
        initWithMediaTypes: MPMediaTypeAnyAudio];                   // 1

[picker setDelegate: self];                                         // 2
[picker setAllowsPickingMultipleItems: YES];                        // 3
picker.prompt =
    NSLocalizedString (@"Add songs to play",
                        "Prompt in media item picker");

[myController presentModalViewController: picker animated: YES];    // 4
[picker release];
```

Here’s how this code works:

1. Creates a media item picker. The parameter indicates the sort of media items to display. For options, see the [Media Item Type Flags](https://developer.apple.com/documentation/mediaplayer/mpmediatype) enumeration.
2. Establishes your controller object as the delegate.
3. Specifies that the user can pick multiple items. You can instead display a single-item picker by excluding this statement; the default behavior is to disallow multiple selection.
4. Displays the picker. The `myController` object retains it so you then release it to balance the `alloc` call.

[Next](Using%20the%20iPod%20Library.md)[Previous](Using%20Media%20Playback.md)

