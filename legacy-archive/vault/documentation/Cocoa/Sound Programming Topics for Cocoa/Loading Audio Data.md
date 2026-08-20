---
title: Sound Programming Topics for Cocoa
apple_id: 10000104i
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AppKit
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sound/Tasks/LoadingAudioData.html
archived_at: '2026-07-15T07:19:16.050525Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sound Programming Topics for Cocoa](Introduction%20to%20Sound%20Programming%20Topics%20for%20Cocoa.md)


[Next](Managing%20Sound%20Playback.md)[Previous](Overview%20of%20the%20NSSound%20Class.md)

# Loading Audio Data

There are several ways to initialize an `NSSound` instance with audio data. Note that `NSSound` objects are immutable so once you have created an instance with one of the `init...` methods, you cannot change the instance or associate different audio data with it.

The simplest way to create an `NSSound` instance is using the `soundNamed:` class method. Named sounds are instances of `NSSound` that have been given a name using the `setName:` method. The `NSSound` class keeps a list of the named instances created by your application, as well as the named system sounds provided by the Application Kit. The system sounds (located in `/System/Library/Sounds`) have been named by the Application Kit using their filenames without the file extension. The following code listing shows you how to load a system sound by name:

```
NSSound *mySound = [NSSound soundNamed:@"Temple"];
```

The `soundNamed:` method first searches for an existing sound file with the name you’ve specified, and if one is found, it is returned to you. Since this example refers to a standard system sound, there is no need to search further.

The following code listing shows you how to load a sound file from disk using `soundNamed:`.

```
NSSound *airplaneSound = [NSSound soundNamed:@"Airplane_44KStereo"];
```

If there is no known sound with the name you’ve specified, `soundNamed:` searches your application’s main bundle, and then the `/Library/Sounds` and `~/Library/Sounds` directories for sound files with the specified name. If no data can be found for _name_, no object is created and `nil` is returned.

Note that once again the file extension is not used when loading sound files using the `soundNamed:` method. Also note that AIFF files must use the `.aiff` file extension (not `.aif`) in order to be located by `soundNamed:`.

If you want to load sound files from someplace in the file system other than your application’s bundle, you can use the method `initWithContentsOfFile:byReference:`. As you would expect, this method attempts to initialize a newly allocated `NSSound` instance with the audio data in the specified file. If the _byReference:_ parameter is `YES`, only the name of the sound is stored with the `NSSound` instance when archived using `encodeWithCoder:`, otherwise the audio data is archived along with the instance. The following code listing shows you how to create an `NSSound` instance and initialize it with a sound file given a pathname to the file.

```
sound = [[NSSound alloc] initWithContentsOfFile:@"/Volumes/Audio/Truck.aiff"
                                    byReference:YES];
```


Loading a sound from a URL is very similar to using a pathname as demonstrated in the section [Loading Sounds By Pathname](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg44dmljzhe2tema). The code listing below shows how to use a URL instead of a pathname. Note that only file system URLs are currently supported.

```
NSURL *soundfileURL = [NSURL fileURLWithPath:@"/Volumes/Audio/Truck.aiff"];
NSSound *sound = [[NSSound alloc] initWithContentsOfURL:soundfileURL
                                            byReference:NO];
```


Listing 1 shows how to load a sound file using an `NSOpenPanel` object.

__Listing 1__  Loading a sound file using an open dialog

```objc
- (IBAction)loadSoundOpenPanel:(id)sender
{
    int result;
    NSOpenPanel *oPanel = [NSOpenPanel openPanel];
    NSArray *filesToOpen;
    NSString *theFileName;
    NSMutableArray *fileTypes = [NSSound soundUnfilteredTypes];
        // All file types NSSound understands

    [oPanel setAllowsMultipleSelection:NO];

    result = [oPanel runModalForDirectory:NSHomeDirectory() file:nil
             types:fileTypes];

    if (result == NSOKButton) {
        filesToOpen = [oPanel filenames];
        theFileName = [filesToOpen objectAtIndex:0];
        NSLog(@"Open Panel Returned: %@.\n", theFileName);

        [self _loadSoundFromPath:theFileName];
    } else
        [infoTextField setStringValue:@"Sound failed to load..."];
}
```

[Next](Managing%20Sound%20Playback.md)[Previous](Overview%20of%20the%20NSSound%20Class.md)

