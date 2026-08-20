---
title: Using NSSound with CoreAudio on Mac OS 10.3.x
apple_id: DTS10003675
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AppKit
published: '2006-03-29'
source_url: https://developer.apple.com/library/archive/qa/qa1394/_index.html
archived_at: '2026-07-18T02:30:31.345959Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1394

# Using NSSound with CoreAudio on Mac OS 10.3.x

## Q:  I am using `NSSound` with CoreAudio on Mac OS 10.3.x, why am I getting NULL data in my IOProc callback?

A: Some applications might find it useful to use Application Kit framework's `NSSound` and Core Audio within the same application. A developer must take notice that `NSSound` might interfere with Core Audio's HAL (Hardware Abstraction Layer) IOProc.

On MacOS 10.3.x systems, using the `NSSound` class in the same process as a Core Audio framework IOProc callback can yield NULL input buffers in the IOProc callback (rdar://4106975). This bug affects applications that add a Core Audio IOProc on the same device that `NSSound` is using for its sound output: the Default Output Audio Device. Applications that make calls to `NSSound` before adding a Core Audio IOProc to the audio device, will get NULL input buffers in the Core Audio IOProc.

To workaround this problem, the process needs to make its calls to `AudioDeviceAddIOProc` before making any calls to `NSSound`.

__Listing 1__  Sample problem

```objc
#import <Cocoa/Cocoa.h>
#import <CoreAudio/CoreAudio.h>

OSStatus recordIOProc ( AudioDeviceID inDevice,
                        const AudioTimeStamp* inNow,
                        const AudioBufferList* inInputData,
                        const AudioTimeStamp* inInputTime,
                        AudioBufferList* outOutputData,
                        const AudioTimeStamp* inOutputTime,
                        void* inClientData )
{
    if ( inInputData )
    {
        if ( inInputData->mBuffers[0].mData == NULL )
            NSLog (@"CoreAudio IOProc is being given NULL input buffers");
    }

    return noErr;
}

int main()
{
    NSAutoreleasePool * pool = [NSAutoreleasePool new];
    AudioDeviceID device;

    UInt32 theSize = sizeof(AudioDeviceID);
    verify_noerr( AudioHardwareGetProperty ( kAudioHardwarePropertyDefaultInputDevice, &theSize, & device ) );

    NSSound *sound = [[NSSound alloc] initWithContentsOfFile:
                                  @"/System/Library/Sounds/Submarine.aiff" byReference:NO];
   [sound play];

    verify_noerr( AudioDeviceAddIOProc ( device, recordIOProc, NULL ) );
    verify_noerr( AudioDeviceStart ( device, recordIOProc ) );

    [[NSRunLoop currentRunLoop] runUntilDate:[NSDate dateWithTimeIntervalSinceNow:2]];

    verify_noerr( AudioDeviceStop ( device, recordIOProc ) );
    verify_noerr( AudioDeviceRemoveIOProc ( device, recordIOProc ) );

    [sound release];

    [pool release];
    return 0;
}
```

When running the above sample code, you will see "CoreAudio IOProc is being given NULL input buffers" printed many many times in the program's standard output (stdout).

To workaround this problem, the process needs to make its calls to `AudioDeviceAddIOProc` before making any calls to `NSSound`. The following modified version of the above sample code shows this:

__Listing 2__  Workaround

```objc
#import <Cocoa/Cocoa.h>
#import <CoreAudio/CoreAudio.h>

OSStatus recordIOProc ( AudioDeviceID inDevice,
                        const AudioTimeStamp* inNow,
                        const AudioBufferList* inInputData,
                        const AudioTimeStamp* inInputTime,
                        AudioBufferList* outOutputData,
                        const AudioTimeStamp* inOutputTime,
                        void* inClientData )
{
    if ( inInputData )
    {
        if ( inInputData->mBuffers[0].mData == NULL )
            NSLog (@"CoreAudio IOProc is being given NULL input buffers");
    }

    return noErr;
}

int main()
{
    NSAutoreleasePool * pool = [NSAutoreleasePool new];
    AudioDeviceID device;

    UInt32 theSize = sizeof(AudioDeviceID);
    verify_noerr( AudioHardwareGetProperty ( kAudioHardwarePropertyDefaultInputDevice, &theSize, & device ) );

    //Call this *before* using NSSound
    verify_noerr( AudioDeviceAddIOProc ( device, recordIOProc, NULL ) );

    NSSound *sound = [[NSSound alloc] initWithContentsOfFile:
                                   @"/System/Library/Sounds/Submarine.aiff" byReference:NO];
    [sound play];

    verify_noerr( AudioDeviceStart ( device, recordIOProc ) );

    [[NSRunLoop currentRunLoop] runUntilDate:[NSDate dateWithTimeIntervalSinceNow:2]];

    verify_noerr( AudioDeviceStop ( device, recordIOProc ) );
    verify_noerr( AudioDeviceRemoveIOProc ( device, recordIOProc ) );

    [sound release];

    [pool release];
    return 0;
}
```

Notice that the only change that's been made here is that we've moved the `AudioDeviceAddIOProc` call to before the `NSSound` calls. When running this sample code, recordIOProc will not print out the string "CoreAudio IOProc is being given NULL input buffers", indicating that it is receiving valid input buffers.

Note that it is not necessary to call `AudioDeviceStart` before any calls to `NSSound`. It is only necessary to call `AudioDeviceAddIOProc`.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-03-29 | Formatting changes only. |
| 2005-06-30 | New document that workaround the NULL input buffers in a Core Audio IOProc callback when using NSSound by using AudioDeviceAddIOProc |

