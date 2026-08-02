---
title: QTKit Application Tutorial
apple_id: TP40008155
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2016-08-26'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/QTKitApplicationTutorial/AddingAudioInputandDVCameraSupport/AddingAudioInputandDVCameraSupport.html
archived_at: '2026-07-15T07:18:13.450676Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QTKit Application Tutorial](Introduction.md)


[Next](Creating%20a%20QTKit%20Stop%20Motion%20Application.md)[Previous](Building%20a%20Simple%20QTKit%20Recorder%20Application.md)

# Adding Audio Input and DV Camera Support

If you worked through the sequence of steps outlined in the previous chapter, you’re now ready to extend the functionality of your QTKit recorder application.

In this chapter, you add audio input capability to your recorder application, as well as support for input from DV cameras. This is accomplished with only a dozen lines of [Objective-C](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectiveC.html#//apple_ref/doc/uid/TP40008195-CH43) code, with error handling included.

Add audio input capability and video input from DV cameras:

1. Launch Xcode 3.2 and open your MyRecorder project.

   - Click the `MyRecorderController.h` declaration file.
   - Replace the `mCaptureDeviceInput` instance variable with these instance variables.

```
QTCaptureDeviceInput        *mCaptureVideoDeviceInput;
QTCaptureDeviceInput        *mCaptureAudioDeviceInput;
```

     These are the audio and video input device variables that enable you to record audio, as well as video from external DV cameras.

   At this point, your code should look like this:

```objc
#import <Cocoa/Cocoa.h>
#import <QTKit/QTKit.h>

@interface MyRecorderController : NSObject {
    IBOutlet QTCaptureView      *mCaptureView;

    QTCaptureSession            *mCaptureSession;
    QTCaptureMovieFileOutput    *mCaptureMovieFileOutput;
    QTCaptureDeviceInput        *mCaptureVideoDeviceInput;
    QTCaptureDeviceInput        *mCaptureAudioDeviceInput;
}
- (IBAction)startRecording:(id)sender;
- (IBAction)stopRecording:(id)sender;

@end
```


Now open your `MyRecorderController.m` implementation file.

1. Scroll down to the code block that begins with `QTCaptureDevice *videoDevice`.

   - Find a video input device, such as the iSight camera, and open it.

```
QTCaptureDevice *videoDevice = [QTCaptureDevice defaultInputDeviceWithMediaType:QTMediaTypeVideo];
success = [videoDevice open:&error];
```
2. If you can’t find or open a video input device, try to find and open a muxed video input device, such as a DV camera.

   Note that in a muxed video, the audio and video tracks are mixed together.

```
    if (!success) {
        videoDevice = [QTCaptureDevice defaultInputDeviceWithMediaType:QTMediaTypeMuxed];
        success = [videoDevice open:&error];
}
if (!success) {
   [videoDevice = nil;
}
if (videoDevice) {
```
3. Add support for audio from an audio input device to the capture session.

   Note that you added an audio type of `QTMediaTypeSound` to the video device to handle the chores of capturing your audio stream in your capture session.

```
        mCaptureVideoDeviceInput = [[QTCaptureDeviceInput alloc] initWithDevice:videoDevice];
        success = [mCaptureSession addInput:mCaptureVideoDeviceInput error:&error];
        if (!success) {
        }

        if (![videoDevice hasMediaType:QTMediaTypeSound] && ![videoDevice hasMediaType:QTMediaTypeMuxed]) {

            QTCaptureDevice *audioDevice = [QTCaptureDevice defaultInputDeviceWithMediaType:QTMediaTypeSound];
            success = [audioDevice open:&error];

            if (!success) {
                audioDevice = nil;
            }

            if (audioDevice) {
                mCaptureAudioDeviceInput = [[QTCaptureDeviceInput alloc] initWithDevice:audioDevice];

                success = [mCaptureSession addInput:mCaptureAudioDeviceInput error:&error];
                if (!success) {
                }
            }
        }
```
4. Create the movie file output and add it to the session.

```
        mCaptureMovieFileOutput = [[QTCaptureMovieFileOutput alloc] init];
        success = [mCaptureSession addOutput:mCaptureMovieFileOutput error:&error];
        if (!success) {
        }
```
5. Associate the capture view in the UI with the session.

```
        [mCaptureView setCaptureSession:mCaptureSession];

        [mCaptureSession startRunning];
    }

}
```
6. Handle window closing notifications for your device input.

```objc
- (void)windowWillClose:(NSNotification *)notification
{
    [mCaptureSession stopRunning];
    if ([[mCaptureVideoDeviceInput device] isOpen])
        [[mCaptureVideoDeviceInput device] close];
    if ([[mCaptureAudioDeviceInput device] isOpen])
        [[mCaptureAudioDeviceInput device] close];
}
```
7. Deallocate memory for your capture objects.

```objc
- (void)dealloc
{
    [mCaptureSession release];
    [mCaptureVideoDeviceInput release];
    [mCaptureAudioDeviceInput release];
    [mCaptureMovieFileOutput release];

    [super dealloc];
}
```
8. Add these start and stop recording actions.

```objc
- (IBAction)startRecording:(id)sender
.
.
.
- (IBAction)stopRecording:(id)sender
}
```
9. Specify the output destination for your recorded media, in this case, a QuickTime movie.

   - Insert the block of code inside the IB `startRecording:` and `stopRecording:` actions in the previous step.

```objc
{
    [mCaptureMovieFileOutput recordToOutputFileURL:[NSURL fileURLWithPath:@"/Users/Shared/My Recorded Movie.mov"]];
}
{
    [mCaptureMovieFileOutput recordToOutputFileURL:nil];
- (void)captureOutput:(QTCaptureFileOutput *)captureOutput didFinishRecordingToOutputFileAtURL:(NSURL *)outputFileURL forConnections:(NSArray *)connections dueToError:(NSError *)error
{
    [[NSWorkspace sharedWorkspace] openURL:outputFileURL];
}

@end
```

Now build and compile your extended QTKit recorder application. After you launch the application, you can begin to capture audio from your iSight camera or audio/video from a DV camera. The output is again recorded as a QuickTime movie and then automatically opened in QuickTime Player on your desktop.

[Next](Creating%20a%20QTKit%20Stop%20Motion%20Application.md)[Previous](Building%20a%20Simple%20QTKit%20Recorder%20Application.md)

