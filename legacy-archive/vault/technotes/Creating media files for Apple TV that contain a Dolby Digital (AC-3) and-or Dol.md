---
title: Creating media files for Apple TV that contain a Dolby Digital (AC-3) and/or
  Dolby Digital Plus (Enhanced AC-3) audio track
apple_id: DTS40016929
resource_type: Technical Note
platform: tvOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-04-04'
source_url: https://developer.apple.com/library/archive/technotes/tn2429/_index.html
archived_at: '2026-07-26T19:54:15.126110Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2429

# Creating media files for Apple TV that contain a Dolby Digital (AC-3) and/or Dolby Digital Plus (Enhanced AC-3) audio track

Discusses requirements for authoring movie files for the Apple TV containing Dolby Digital and/or Dolby Digital Plus audio. Describes different workflows to create compatible files using either `AVMutableMovie` or `AVAssetWriter`, and provides code examples for each.

Apple TV supports the playback of .mov and .m4v files containing Dolby Digital (AC-3) and/or Dolby Digital Plus (Enhanced AC-3) encoded audio. Application developers can use the AVFoundation framework along with the techniques discussed in this document to create Apple TV compatible movie files containing Dolby Digital and/or Dolby Digital Plus audio.

__Note:__ For information about authoring media containing Dolby Digital and/or Dolby Digital Plus encoded audio that will be streamed to the Apple TV using HTTP Live Streaming see the [HLS Authoring Specification for Apple TV](https://developer.apple.com/library/tvos/documentation/General/Reference/HLSAuthoringSpec/Requirements.html).

[Use a Chain of Fallback Track References for Movies Containing Special-Purpose Encodings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmojshewugsbrfvkvgrk7ifpugscbjfhf6t2gl5dectcmijaugs27krjecq2ll5jekrsfkjcu4q2fknpumt2sl5gu6vsjivjv6q2pjzkecskojfheox2tkbcugskbjrpvavkskbhvgrk7ivhegt2ejfheouy)[Requirements for Apple TV Media Files containing Dolby Digital Audio](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmojshewugsbrfvjekukvjfjektkfjzkfgx2gj5jf6qkqkbgekx2ukzpu2rkejfav6rsjjrcvgx2dj5hfiqkjjzeu4r27l5ce6tcclfpuiskhjfkectc7ifkuiskp)[Use Fallback Track References for Apple TV Media Files containing Dolby Digital Audio](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmojshewugsbrfvjekukvjfjektkfjzkfgx2gj5jf6qkqkbgekx2ukzpu2rkejfav6rsjjrcvgx2dj5hfiqkjjzeu4r27l5ce6tcclfpuiskhjfkectc7ifkuiskpfvkvgrk7izauytccifbuwx2ukjaugs27kjcumrksivhegrktl5de6us7ififatcfl5kfmx2nivcesqk7izeuyrktl5bu6tsuifeu4skoi5puit2mijmv6rcji5eviqkml5avkrcjj4)[Related Tracks must be members of the same Alternate Group](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmojshewugsbrfvjekukvjfjektkfjzkfgx2gj5jf6qkqkbgekx2ukzpu2rkejfav6rsjjrcvgx2dj5hfiqkjjzeu4r27l5ce6tcclfpuiskhjfkectc7ifkuiskpfvjektcbkrcuix2ukjaugs2tl5gvku2ul5bekx2nivguerksknpu6rs7kreekx2tifgukx2bjrkekusoifkekx2hkjhvkua)[It is good practice to encode the audio for both tracks at the same sample rate (48kHz is normal)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmojshewugsbrfvjekukvjfjektkfjzkfgx2gj5jf6qkqkbgekx2ukzpu2rkejfav6rsjjrcvgx2dj5hfiqkjjzeu4r27l5ce6tcclfpuiskhjfkectc7ifkuiskpfvevix2jknpuot2pirpvausbinkesq2fl5ke6x2fjzbu6rcfl5keqrk7ifkuiskpl5de6us7ijhvisc7krjecq2lknpucvc7kreekx2tifgukx2tifgvatcfl5jecvcfl5ptiocljbnf6sktl5he6usnifgf6)[Requirements for Apple TV Media Files containing Dolby Digital Plus Audio](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmojshewugsbrfvjekukvjfjektkfjzkfgx2gj5jf6qkqkbgekx2ukzpu2rkejfav6rsjjrcvgx2dj5hfiqkjjzeu4r27l5ce6tcclfpuiskhjfkectc7kbgfku27ifkuiskp)[Using AVMutableMovie to assemble Apple TV media files containing Dolby Digital or Dolby Digital Plus audio](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmojshewugsbrfvkvgskoi5pucvsnkvkecqsmivgu6vsjivpvit27ifjvgrknijgekx2bkbieyrk7krlf6tkfireucx2gjfgeku27inhu4vcbjfhestshl5ce6tcclfpuiskhjfkectc7j5jf6rcpjrbfsx2ejfdusvcbjrpvatcvknpucvkejfhq)[Using AVAssetWriter to create Apple TV media files containing Dolby Digital and/or Dolby Digital Plus audio](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmojshewugsbrfvkvgskoi5pucvsbknjukvcxkjevirksl5ke6x2dkjcucvcfl5avaucmivpvivs7jvcuiskbl5destcfknpugt2okraustsjjzdv6rcpjrbfsx2ejfdusvcbjrpuctsel5hvex2ej5geewk7ireuoskuifgf6ucmkvjv6qkvireu6)[Creating a Fallback Track Association with AVAssetWriterInput](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmojshewugsbrfvkvgskoi5pucvsbknjukvcxkjevirksl5ke6x2dkjcucvcfl5avaucmivpvivs7jvcuiskbl5destcfknpugt2okraustsjjzdv6rcpjrbfsx2ejfdusvcbjrpuctsel5hvex2ej5geewk7ireuoskuifgf6ucmkvjv6qkvireu6lkdkjcucvcjjzdv6qk7izauytccifbuwx2ukjaugs27ifjvgt2djfaviskpjzpvoskujbpucvsbknjukvcxkjevirksjfhfavku)[Creating Track Groups with AVAssetWriterInputGroup](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmojshewugsbrfvkvgskoi5pucvsbknjukvcxkjevirksl5ke6x2dkjcucvcfl5avaucmivpvivs7jvcuiskbl5destcfknpugt2okraustsjjzdv6rcpjrbfsx2ejfdusvcbjrpuctsel5hvex2ej5geewk7ireuoskuifgf6ucmkvjv6qkvireu6lkdkjcucvcjjzdv6vcsifbuwx2hkjhvkuctl5lusvcil5avmqktkncviv2sjfkekusjjzifkvchkjhvkua)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmojshewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Use a Chain of Fallback Track References for Movies Containing Special-Purpose Encodings

Playback support for special-purpose audio encodings in a QuickTime movie file (such as Dolby Digital audio) may not be available across all platforms and devices. In general, any audio track for which support is not expected to be available in all playback contexts, whether that support is to be provided by decoding the audio on the playback device or by passing the encoded audio through an output to an outboard decoder, should be accompanied by an audio track that encodes the same content and for which support is expected to be generally available.

In such cases, you should create a chain of two or more audio tracks, which generally proceeds, by means of fallback (`‘fall’`) track references, from the least widely supported audio encoding to the most widely supported audio encoding. The audio track that terminates the chain has no fallback track references; all non-terminal audio tracks in the chain must have exactly one fallback track reference. In addition, the terminal track in the chain must be enabled by default and all others in the chain must be disabled.

For complete information about track references in QuickTime movies, see the [QuickTime File Format specification](https://developer.apple.com/library/mac/documentation/QuickTime/QTFF/QTFFPreface/qtffPreface.html).

[Back to Top](#)

## Requirements for Apple TV Media Files containing Dolby Digital Audio

### Use Fallback Track References for Apple TV Media Files containing Dolby Digital Audio

When authoring a movie containing Dolby Digital audio, a fallback track reference to a generally supported encoding (Stereo) must be included in accordance with the guidelines just discussed. Here’s an example of such a movie containing two audio tracks, Dolby Digital audio and Stereo:

- AAC Encoded Stereo - This is the standard Stereo audio track
- AC-3 - This is the Dolby Digital audio track.

In this movie, a fallback track reference must exist that allows the appropriate generally supported audio track (Stereo) to be directly identified for the track that may not be supported in all playback contexts (Dolby Digital). Marking the Stereo track as the fallback for the Dolby Digital track will ensure that devices not capable of playing Dolby Digital audio can still play an equivalent track. This represents the simplest case of a chain of (2) related tracks with fallback references.

In addition, based on the guidelines for fallback references, the terminal track in the chain must be enabled by default and all others in the chain must be disabled. Therefore, the default track state properties must be set as follows:

- The AAC Stereo audio track must be enabled by default
- The Dolby Digital track must be disabled by default.

### Related Tracks must be members of the same Alternate Group

In an Apple TV movie file containing a Dolby Digital audio track and Stereo audio track with the appropriate fallback references, both tracks must also be members of the same alternate group.

Alternate groups are collections of tracks that all serve the same purpose, either in a QuickTime movie or MPEG-4 file, where any track in the group can be substituted for another.

General guidelines for the use of alternate groups in movies to be played on Apple devices include:

- The group must contain only audio tracks, only video tracks, or only legible tracks (i.e. subtitle, text, or closed caption tracks).
- Typically, all tracks of the same type will be placed into a single alternate group.
- One track in the group must be enabled.
- All other tracks in the group must be disabled.

See the [QuickTime File Format specification](https://developer.apple.com/library/mac/documentation/QuickTime/QTFF/QTFFPreface/qtffPreface.html) for complete information about the use of alternate groups in QuickTime movies.

### It is good practice to encode the audio for both tracks at the same sample rate (48kHz is normal)

While not a strict requirement, if both the Dolby Digital and Stereo audio tracks have different sample rates the Apple TV may default to the sample rate of the Dolby Digital audio track. If the AAC stereo audio track is being used for playback and has a different sample rate from the Dolby Digital audio track (for example, the sample rate of the AAC track is 44.1kHz and the Dolby Digital track is 48kHz) the AAC track may be sample rate converted to 48kHz for output.

To avoid this sample rate conversion by the output device, content authors should encode both audio tracks at the same sample rate.

[Back to Top](#)

## Requirements for Apple TV Media Files containing Dolby Digital Plus Audio

Dolby Digital Plus can either be accommodated by a similar simple fallback track reference chain as described above, falling back directly from Dolby Digital Plus to Stereo, or by a longer chain that indicates that fallback should proceed first to evaluate the suitability of a Dolby Digital (AC-3) fallback, falling back all the way to Stereo only when both Dolby Digital Plus and Dolby Digital are unsupported. All such tracks in a given chain must also be members of the same alternate group. The terminal track in the chain must be enabled by default and all others in the chain must be disabled.

__Note:__ Movie files purchased from the iTunes store containing Dolby Digital and/or Dolby Digital Plus encoded audio employ track groups and track references as described in this document and are fully compatible across all generations of Apple TV devices.

[Back to Top](#)

## Using AVMutableMovie to assemble Apple TV media files containing Dolby Digital or Dolby Digital Plus audio

You can use `AVMutableMovie` to assemble a QuickTime movie containing Dolby Digital and/or Dolby Digital Plus audio from a pre-encoded Apple TV compliant .m4v or .mov file and a Dolby Digital and/or Dolby Digital Plus .ac3 file. Listing 1 demonstrates how to assemble an Apple TV compliant QuickTime movie file using Swift code and Listing 2 shows the equivalent function in Objective-C code. The function assumes Apple TV compliant media has been created and saved to an .m4v or .mov file, and a Dolby Digital or Dolby Digital Plus .ac3 audio file has been created. The audio track in the .ac3 audio file is then combined with the audio and video track in the provided .mov or .m4v file to produce a new well interleaved, fast-start movie file conforming to the track requirements discussed in this document ready to sync with the Apple TV.

__Listing 1__  How to assemble an Apple TV compliant QuickTime movie file containing Dolby Digital or Dolby Digital Plus audio (Swift).

```objc
import Cocoa
import AVFoundation

/*

 createAppleTVMovie

 Parameters:

 srcMovieURL
 A URL to a Apple TV conforming .mov or .m4v media file containing an AAC stereo audio
 track and a video track.

 srcAC3URL
 A URL to a Dolby Digital .ac3 audio file.

 dstMovieURL
 A file URL where a new movie file will be written containing the source Apple TV
 AAC stereo track and video track combined with the AC3 audio track from the provided
 .ac3 audio file.

 Discussion:

 This function creates a new, well interleaved, fast-start Apple TV compatible file
 containing the Apple TV conforming source movie's AAC stereo track and video track
 combined with the AC3 audio track from the provided .ac3 audio file.

 The resulting flattened movie file will have the required Apple TV audio track layout:

 Two audio tracks:
 - AAC stereo, and must be enabled
 - AC-3 track for surround, and be disabled
 - Fallback track association from the AC-3 audio track to the AAC track
 - Both tracks are members of the same alternate group

 */

-(void)createAppleTVMovie:(NSURL *)srcMovieURL
                  ac3File:(NSURL *)srcAC3URL
                    toURL:(NSURL *)dstMovieURL
{
    /*
     Create a new mutable movie into which we will combine all the tracks
     from the source files to create a new interleaved, fast-start
     movie compatible with the Apple TV.
     */
    AVMutableMovie *dstMovie = [[AVMutableMovie alloc ]init];

    AVMovie *srcMovie = [AVMovie movieWithURL:srcMovieURL options:nil];
    // Get the AAC audio track from the source movie.
    AVMovieTrack *srcAACTrack =
        [[srcMovie tracksWithMediaType:AVMediaTypeAudio] firstObject];
    CMFormatDescriptionRef formatDesc =
    (__bridge CMFormatDescriptionRef)([[srcAACTrack formatDescriptions] firstObject]);
    // Verify the source movie file contains an actual AAC track.
    BOOL foundAACMedia = false;
    switch (CMFormatDescriptionGetMediaSubType(formatDesc)) {
        case kAudioFormatMPEG4AAC:
        case kAudioFormatMPEG4AAC_HE:
        case kAudioFormatMPEG4AAC_LD:
        case kAudioFormatMPEG4AAC_ELD:
        case kAudioFormatMPEG4AAC_ELD_SBR:
        case kAudioFormatMPEG4AAC_ELD_V2:
        case kAudioFormatMPEG4AAC_HE_V2:
        case kAudioFormatMPEG4AAC_Spatial:

            foundAACMedia = true;
            break;

        default:
            break;
    }
    if (!foundAACMedia) {
        NSLog(@"Failed to find an AAC audio track in the source movie file.");
        return;
    }

    // Get first video track in the source movie.
    AVMovieTrack *srcVideoTrack =
    [[srcMovie tracksWithMediaType:AVMediaTypeVideo] firstObject];
    if (!srcVideoTrack) {
        NSLog(@"Failed to find a video track in the source movie.");
        return;
    }

    AVAsset *srcAC3Asset = [AVURLAsset URLAssetWithURL:srcAC3URL
            options:[NSDictionary dictionaryWithObject:[NSNumber numberWithBool:YES]
                    forKey:AVURLAssetPreferPreciseDurationAndTimingKey]];
    // Get the AC3 track in the source file.
    AVAssetTrack *srcAC3Track = [[srcAC3Asset tracks] firstObject];
    formatDesc =
    (__bridge CMFormatDescriptionRef)([[srcAC3Track formatDescriptions] firstObject]);
    // Verify the AC-3 source file contains an actual AC-3 track.
    if (CMFormatDescriptionGetMediaSubType(formatDesc) != kAudioFormatAC3)
    {
        NSLog(@"AC-3 track not found in the source file.");
        return;
    }

    // Add a new audio track containing the AC-3 track references to the movie.
    AVMutableMovieTrack *destAC3Track =
    [self addTrackReferencesToMovie:srcAC3Track
                                 toMovie:dstMovie
                                mediaType:AVMediaTypeAudio];
    // Add a new audio track containing the AAC track references to the movie.
    AVMutableMovieTrack *destAACTrack =
    [self addTrackReferencesToMovie:srcAACTrack
                                 toMovie:dstMovie
                               mediaType:AVMediaTypeAudio];
    // Add a new video track containing the video track references to the movie.
    [self addTrackReferencesToMovie:srcVideoTrack
                                 toMovie:dstMovie
                               mediaType:AVMediaTypeVideo];

    /*
     Create a "fallback" track association from the AAC audio track to the AC-3
     track.
     */
    [destAC3Track addTrackAssociationToTrack:destAACTrack
                                        type:AVTrackAssociationTypeAudioFallback];

    /*
        Set both audio tracks as members of an alternate group. Use the
        alternateGroupID of the AAC track, if it's already part of a track group.
    */
    NSInteger audioAlternateGroupID = destAACTrack.alternateGroupID;
    if (audioAlternateGroupID == 0) {
        /*
         Not already part of a track group. Create a new group by assigning both tracks an
         unused, non-zero alternate group ID.
         */
        audioAlternateGroupID = 1;
        for (AVAssetTrackGroup *trackGroup in [dstMovie trackGroups]) {
            CMPersistentTrackID trackIDOfTrackInGroup =
            (CMPersistentTrackID)[[[trackGroup trackIDs] firstObject] intValue];
            AVMovieTrack *trackInGroup =
            [dstMovie trackWithTrackID:trackIDOfTrackInGroup];
            NSInteger trackGroupAlternateGroupID = [trackInGroup alternateGroupID];
            if (trackGroupAlternateGroupID >= audioAlternateGroupID) {
                audioAlternateGroupID = trackGroupAlternateGroupID + 1;
            }
        }
        destAACTrack.alternateGroupID = audioAlternateGroupID;
    }
    destAC3Track.alternateGroupID = audioAlternateGroupID;

    /*
     Disable the AC-3 track since it is not the terminal track in the
     fallback reference chain.
     */
    [destAC3Track setEnabled:false];
    /*
     Enable the AAC track since it is the terminal track in the fallback
     reference chain.
     */
    [destAACTrack setEnabled:true];

    /*
     When creating content that carries multiple audio tracks with different languages,
     the implementation should not match just any AAC track with the newly associated
     AC-3 audio, but an AAC track with values for the track properties languageCode and
     extendedLanguageTag that match the language of the AC-3 audio.

     However, even if the content carries audio in just one language, as these listings
     assume, it's necessary to ensure that the newly added AC-3 track has the same
     languageCode and extendedLanguageTag as the previously existing AAC track that's
     associated with it. This will ensure that automatic and manual media selection
     behave correctly in all of their various use cases.

     Below we're assuming that the language of the AC-3 audio really does match that of
     the AAC audio, but a real implementation that's trying to create multilingual content
     would exercise appropriate care as just discussed.
     */
    destAC3Track.languageCode = destAACTrack.languageCode;
    destAC3Track.extendedLanguageTag = destAACTrack.extendedLanguageTag;

    // Use AVAssetExportSession to create a well interleaved, fast-start movie.
    AVAssetExportSession *exportSession =
        [[AVAssetExportSession alloc] initWithAsset:dstMovie
            presetName:AVAssetExportPresetPassthrough];

    exportSession.outputURL = dstMovieURL;
    exportSession.outputFileType = AVFileTypeQuickTimeMovie;
    // Indicates the movie should support "fast start".
    exportSession.shouldOptimizeForNetworkUse = YES;

    // Perform the export operation to create the new movie file.
    [exportSession exportAsynchronouslyWithCompletionHandler:^(void){
        switch (exportSession.status) {
            case AVAssetExportSessionStatusCompleted:
                NSLog(@"Export completed.");
                break;
            case AVAssetExportSessionStatusFailed:
                NSLog(@"Export failed with an error: %@",exportSession.error);
                break;
            default:
                break;
        }
    }];

}

/*

 addTrackReferencesToMovie

 Add a new track to the movie, and copy the sample data references
 from the provided track to the new track.

*/
-(AVMutableMovieTrack *)addTrackReferencesToMovie:(AVAssetTrack *)track toMovie:(AVMutableMovie *)movie mediaType:(NSString *)mediaType
{
    /*
     Add a new track to the movie, and copy the settings from the
     provided track.
     */
    AVMutableMovieTrack *newTrack =
    [movie addMutableTrackWithMediaType:mediaType
                  copySettingsFromTrack:track options:nil];
    // Copy the source track references into the new track.
    NSError *error;
    BOOL success = [newTrack insertTimeRange:track.timeRange
                                     ofTrack:track
                                      atTime:kCMTimeZero
                    /* Only sample data references to the samples in their
                     original container will be added */
                              copySampleData:false
                                       error:&error];
    if (!success) {
        NSLog(@"Error inserting track references into target movie: %@",error);
        return nil;
    }

    return newTrack;
}
```

__Listing 2__  How to assemble an Apple TV compliant QuickTime movie file containing Dolby Digital or Dolby Digital Plus audio (Objective-C).

```objc
#import <Cocoa/Cocoa.h>
#import <AVFoundation/AVFoundation.h>

/*

 createAppleTVMovie

 Parameters:

 srcMovieURL
 A URL to a Apple TV conforming .mov or .m4v media file containing an AAC stereo audio
 track and a video track.

 srcAC3URL
 A URL to a Dolby Digital .ac3 audio file.

 dstMovieURL
 A file URL where a new movie file will be written containing the source Apple TV
 AAC stereo track and video track combined with the AC3 audio track from the provided
 .ac3 audio file.

 Discussion:

 This function creates a new, well interleaved, fast-start Apple TV compatible file
 containing the Apple TV conforming source movie's AAC stereo track and video track
 combined with the AC3 audio track from the provided .ac3 audio file.

 The resulting flattened movie file will have the required Apple TV audio track layout:

 Two audio tracks:
 - AAC stereo, and must be enabled
 - AC-3 track for surround, and be disabled
 - Fallback track association from the AC-3 audio track to the AAC track
 - Both tracks are members of the same alternate group

 */

-(void)createAppleTVMovie:(NSURL *)srcMovieURL
                  ac3File:(NSURL *)srcAC3URL
                    toURL:(NSURL *)dstMovieURL
{
    /*
     Create a new mutable movie into which we will combine all the tracks
     from the source files to create a new interleaved, fast-start
     movie compatible with the Apple TV.
     */
    AVMutableMovie *dstMovie = [[AVMutableMovie alloc ]init];

    AVMovie *srcMovie = [AVMovie movieWithURL:srcMovieURL options:nil];
    // Get the AAC audio track from the source movie.
    AVMovieTrack *srcAACTrack =
        [[srcMovie tracksWithMediaType:AVMediaTypeAudio] firstObject];
    CMFormatDescriptionRef formatDesc =
    (__bridge CMFormatDescriptionRef)([[srcAACTrack formatDescriptions] firstObject]);
    // Verify the source movie file contains an actual AAC track.
    BOOL foundAACMedia = false;
    switch (CMFormatDescriptionGetMediaSubType(formatDesc)) {
        case kAudioFormatMPEG4AAC:
        case kAudioFormatMPEG4AAC_HE:
        case kAudioFormatMPEG4AAC_LD:
        case kAudioFormatMPEG4AAC_ELD:
        case kAudioFormatMPEG4AAC_ELD_SBR:
        case kAudioFormatMPEG4AAC_ELD_V2:
        case kAudioFormatMPEG4AAC_HE_V2:
        case kAudioFormatMPEG4AAC_Spatial:

            foundAACMedia = true;
            break;

        default:
            break;
    }
    if (!foundAACMedia) {
        NSLog(@"Failed to find an AAC audio track in the source movie file.");
        return;
    }

    // Get first video track in the source movie.
    AVMovieTrack *srcVideoTrack =
    [[srcMovie tracksWithMediaType:AVMediaTypeVideo] firstObject];
    if (!srcVideoTrack) {
        NSLog(@"Failed to find a video track in the source movie.");
        return;
    }

    AVAsset *srcAC3Asset = [AVURLAsset URLAssetWithURL:srcAC3URL
            options:[NSDictionary dictionaryWithObject:[NSNumber numberWithBool:YES]
                    forKey:AVURLAssetPreferPreciseDurationAndTimingKey]];
    // Get the AC3 track in the source file.
    AVAssetTrack *srcAC3Track = [[srcAC3Asset tracks] firstObject];
    formatDesc =
    (__bridge CMFormatDescriptionRef)([[srcAC3Track formatDescriptions] firstObject]);
    // Verify the AC-3 source file contains an actual AC-3 track.
    if (CMFormatDescriptionGetMediaSubType(formatDesc) != kAudioFormatAC3)
    {
        NSLog(@"AC-3 track not found in the source file.");
        return;
    }

    // Add a new audio track containing the AC-3 track references to the movie.
    AVMutableMovieTrack *destAC3Track =
    [self addTrackReferencesToMovie:srcAC3Track
                                 toMovie:dstMovie
                                mediaType:AVMediaTypeAudio];
    // Add a new audio track containing the AAC track references to the movie.
    AVMutableMovieTrack *destAACTrack =
    [self addTrackReferencesToMovie:srcAACTrack
                                 toMovie:dstMovie
                               mediaType:AVMediaTypeAudio];
    // Add a new video track containing the video track references to the movie.
    [self addTrackReferencesToMovie:srcVideoTrack
                                 toMovie:dstMovie
                               mediaType:AVMediaTypeVideo];

    /*
     Create a "fallback" track association from the AAC audio track to the AC-3
     track.
     */
    [destAC3Track addTrackAssociationToTrack:destAACTrack
                                        type:AVTrackAssociationTypeAudioFallback];

    /*
        Set both audio tracks as members of an alternate group. Use the
        alternateGroupID of the AAC track, if it's already part of a track group.
    */
    NSInteger audioAlternateGroupID = destAACTrack.alternateGroupID;
    if (audioAlternateGroupID == 0) {
        /*
         Not already part of a track group. Create a new group by assigning both tracks an
         unused, non-zero alternate group ID.
         */
        audioAlternateGroupID = 1;
        for (AVAssetTrackGroup *trackGroup in [dstMovie trackGroups]) {
            CMPersistentTrackID trackIDOfTrackInGroup =
            (CMPersistentTrackID)[[[trackGroup trackIDs] firstObject] intValue];
            AVMovieTrack *trackInGroup =
            [dstMovie trackWithTrackID:trackIDOfTrackInGroup];
            NSInteger trackGroupAlternateGroupID = [trackInGroup alternateGroupID];
            if (trackGroupAlternateGroupID >= audioAlternateGroupID) {
                audioAlternateGroupID = trackGroupAlternateGroupID + 1;
            }
        }
        destAACTrack.alternateGroupID = audioAlternateGroupID;
    }
    destAC3Track.alternateGroupID = audioAlternateGroupID;

    /*
     Disable the AC-3 track since it is not the terminal track in the
     fallback reference chain.
     */
    [destAC3Track setEnabled:false];
    /*
     Enable the AAC track since it is the terminal track in the fallback
     reference chain.
     */
    [destAACTrack setEnabled:true];

    /*
     When creating content that carries multiple audio tracks with different languages,
     the implementation should not match just any AAC track with the newly associated
     AC-3 audio, but an AAC track with values for the track properties languageCode and
     extendedLanguageTag that match the language of the AC-3 audio.

     However, even if the content carries audio in just one language, as these listings
     assume, it's necessary to ensure that the newly added AC-3 track has the same
     languageCode and extendedLanguageTag as the previously existing AAC track that's
     associated with it. This will ensure that automatic and manual media selection
     behave correctly in all of their various use cases.

     Below we're assuming that the language of the AC-3 audio really does match that of
     the AAC audio, but a real implementation that's trying to create multilingual content
     would exercise appropriate care as just discussed.
     */
    destAC3Track.languageCode = destAACTrack.languageCode;
    destAC3Track.extendedLanguageTag = destAACTrack.extendedLanguageTag;

    // Use AVAssetExportSession to create a well interleaved, fast-start movie.
    AVAssetExportSession *exportSession =
        [[AVAssetExportSession alloc] initWithAsset:dstMovie
            presetName:AVAssetExportPresetPassthrough];

    exportSession.outputURL = dstMovieURL;
    exportSession.outputFileType = AVFileTypeQuickTimeMovie;
    // Indicates the movie should support "fast start".
    exportSession.shouldOptimizeForNetworkUse = YES;

    // Perform the export operation to create the new movie file.
    [exportSession exportAsynchronouslyWithCompletionHandler:^(void){
        switch (exportSession.status) {
            case AVAssetExportSessionStatusCompleted:
                NSLog(@"Export completed.");
                break;
            case AVAssetExportSessionStatusFailed:
                NSLog(@"Export failed with an error: %@",exportSession.error);
                break;
            default:
                break;
        }
    }];

}

/*

 addTrackReferencesToMovie

 Add a new track to the movie, and copy the sample data references
 from the provided track to the new track.

*/
-(AVMutableMovieTrack *)addTrackReferencesToMovie:(AVAssetTrack *)track toMovie:(AVMutableMovie *)movie mediaType:(NSString *)mediaType
{
    /*
     Add a new track to the movie, and copy the settings from the
     provided track.
     */
    AVMutableMovieTrack *newTrack =
    [movie addMutableTrackWithMediaType:mediaType
                  copySettingsFromTrack:track options:nil];
    // Copy the source track references into the new track.
    NSError *error;
    BOOL success = [newTrack insertTimeRange:track.timeRange
                                     ofTrack:track
                                      atTime:kCMTimeZero
                    /* Only sample data references to the samples in their
                     original container will be added */
                              copySampleData:false
                                       error:&error];
    if (!success) {
        NSLog(@"Error inserting track references into target movie: %@",error);
        return nil;
    }

    return newTrack;
}
```

[Back to Top](#)

## Using AVAssetWriter to create Apple TV media files containing Dolby Digital and/or Dolby Digital Plus audio

Your app workflow might instead use `AVAssetWriter` to create media files. In this case, it isn't necessary to perform post-processing on a existing movie file using `AVMutableMovie` (as shown in Listing 1) to assemble an Apple TV compatible movie containing a Dolby Digital and/or Dolby Digital Plus track. Instead, to satisfy the Apple TV media file requirements for the use of Dolby Digital and/or Dolby Digital Plus audio, use the `AVAssetWriterInput` `addTrackAssociationWithTrackOfInput`: method to create a fallback track association from the Dolby Digital and/or Dolby Digital Plus track to the AAC track, and the `AVAssetWriterInputGroup` and `AVAssetWriterInput` to create a track group for the AAC and Dolby Digital and/or Dolby Digital Plus track. Disable the Dolby Digital and/or Dolby Digital Plus track with the `AVAssetWriterInput` `marksOutputTrackAsEnabled` property.

You should also set the `AVAssetWriterInput` `languageCode` and `extendedLanguageTag` properties appropriately, ensuring that inputs with an association of type `AVTrackAssociationTypeAudioFallback` are given the same value for `languageCode` and for `extendedLanguageTag`. This will ensure that automatic and manual media selection behave correctly in all of their various use cases.

### Creating a Fallback Track Association with AVAssetWriterInput

Use the `AVAssetWriterInput` `addTrackAssociationWithTrackOfInput`:type: method to create a fallback track association from the Dolby Digital and/or Dolby Digital Plus track to the AAC track. This method associates the track corresponding to the specified input with the track corresponding with the receiver. Use the `AVAssetWriterInput` `marksOutputTrackAsEnabled` property to disable the Dolby Digital and/or Dolby Digital Plus track. Listing 3 and Listing 4 give examples.

__Listing 3__  Creating a Fallback Track Association from the Dolby Digital or Dolby Digital Plus track to the AAC track (Swift).

```
let aacTrackInput:AVAssetWriterInput = <#An asset writer input for the AAC track#>
let ac3TrackInput:AVAssetWriterInput = <#An asset writer input for the AC3 track#>

// Disable the Dolby Digital track per the requirements for fallback track references.
ac3TrackInput.marksOutputTrackAsEnabled = false

/*
You should set the languageCode and extendedLanguageTag properties appropriately,
ensuring that inputs with a fallback association have the same value for each of these
properties. This will ensure that automatic and manual media selection behave correctly
in all use cases.
*/
let langCode = <#An appropriate language code#>
ac3TrackInput.languageCode = langCode
aacTrackInput.languageCode = langCode

let extLangTag = <#An appropriate extended language tag#>
ac3TrackInput.extendedLanguageTag = extLangTag
aacTrackInput.extendedLanguageTag = extLangTag

// Create a fallback track association from the Dolby Digital track to the AAC track.
ac3TrackInput.addTrackAssociationWithTrackOfInput(aacTrackInput,
    type: AVTrackAssociationTypeAudioFallback)
```

__Listing 4__  Creating a Fallback Track Association from the Dolby Digital or Dolby Digital Plus track to the AAC track (Objective-C).

```
AVAssetWriterInput *aacTrackInput = <#An asset writer input for the AAC track#>;
AVAssetWriterInput *ac3TrackInput = <#An asset writer input for the AC3 track#>;

// Disable the Dolby Digital track per the requirements for fallback track references.
ac3TrackInput.marksOutputTrackAsEnabled = NO;

/*
You should set the languageCode and extendedLanguageTag properties appropriately,
ensuring that inputs with a fallback association have the same value for each of these
properties. This will ensure that automatic and manual media selection behave correctly
in all use cases.
*/
NSString *langCode = <#An appropriate language code#>;
ac3TrackInput.languageCode = langCode;
aacTrackInput.languageCode = langCode;

NSString *extLangTag = <#An appropriate extended language tag#>;
ac3TrackInput.extendedLanguageTag = extLangTag;
aacTrackInput.extendedLanguageTag = extLangTag;

// Create a fallback track association from the Dolby Digital track to the AAC track.
[ac3TrackInput addTrackAssociationWithTrackOfInput: aacTrackInput
                            type: AVTrackAssociationTypeAudioFallback];
```

### Creating Track Groups with AVAssetWriterInputGroup

The `AVAssetWriterInputGroup` class associates tracks corresponding to inputs with each other in a mutually exclusive relationship for playback or other processing. To create an asset with both AAC and Dolby Digital or Dolby Digital Plus audio tracks – and only one track should be played at a time – group the inputs corresponding to those tracks into a single instance of `AVAssetWriterInputGroup` and add the group to the `AVAssetWriter` instance using the `AVAssetWriter` method `addInputGroup`:. If the output format supports mutually exclusive relationships among tracks, the `AVAssetWriter` marks the tracks as mutually exclusive to each other. Listing 5 and Listing 6 give examples.

__Important:__ You should also set the `AVAssetWriter` `shouldOptimizeForNetworkUse` property to indicate the output file should be written in way that makes it more suitable for playback over a network (also known as "fast-start").

__Listing 5__  Creating a track group with `AVAssetWriterInputGroup` for the AAC track and the Dolby Digital or Dolby Digital Plus track (Swift).

```
let myAssetWriter:AVAssetWriter = <#An asset writer#>

let aacTrackInput:AVAssetWriterInput = <#An asset writer input for the AAC track#>
let ac3TrackInput:AVAssetWriterInput = <#An asset writer input for the AC3 track#>
let trackInputs: [AVAssetWriterInput] = [ aacTrackInput, ac3TrackInput ]

/*
Create and initialize an instance of an asset writer input group for the AC-3 and AAC
tracks.
*/
let inputGroup = AVAssetWriterInputGroup(inputs: trackInputs, defaultInput: aacTrackInput)

myAssetWriter.shouldOptimizeForNetworkUse = true // Create a fast-start file.

// Add the asset writer input group instance to the asset writer.
myAssetWriter.addInputGroup(inputGroup)
```

__Listing 6__  Creating a track group with `AVAssetWriterInputGroup` for the AAC track and the Dolby Digital or Dolby Digital Plus track (Objective-C).

```
AVAssetWriter *myAssetWriter = <#An asset writer#>;

AVAssetWriterInput *aacTrackInput = <#An asset writer input for the AAC track#>;
AVAssetWriterInput *ac3TrackInput = <#An asset writer input for the AC3 track#>;
NSArray *trackInputs = @[ aacTrackInput, ac3TrackInput ];

/*
Create and initialize an instance of an asset writer input group for the AC-3 and AAC
tracks.
*/
AVAssetWriterInputGroup *inputGroup =
     [AVAssetWriterInputGroup assetWriterInputGroupWithInputs: trackInputs
                                                     defaultInput: aacTrackInput];

myAssetWriter.shouldOptimizeForNetworkUse = YES; // Create a fast-start file.

// Add the asset writer input group instance to the asset writer.
[myAssetWriter addInputGroup: inputGroup];
```

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-04-04 | New document that shows how to create media files for Apple TV that contain a Dolby Digital (AC-3) and/or Dolby Digital Plus (Enhanced AC-3) audio track |

