---
title: Speech Programming Topics
apple_id: 10000178i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2003-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Speech/Articles/SynthesizeSpeech.html
archived_at: '2026-07-15T07:19:18.157595Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Speech Programming Topics](Introduction%20to%20Speech.md)


[Next](Recognizing%20Speech.md)[Previous](Introduction%20to%20Speech.md)

# Synthesizing Speech

By using an NSSpeechSynthesizer object, you can make your application speak a word, phrase, or sentence to the user. This synthesized speech is an essential aid to those users with attention or vision disabilities. It is also useful when you want to draw the user’s attention to something important when he or she might be distracted by something else on the screen.

Using an NSSpeechSynthesizer object to “pronounce” text is easy. You initialize the object with a voice and send a `startSpeakingString:` message to it, passing in an NSString object representing the text to speak. Optionally, you can implement one of several delegation methods either to accompany the words pronounced in some interactive fashion or to do something application-specific when speaking concludes.

The essential attribute of an NSSpeechSynthesizer object is a voice. Speech Synthesis defines a number of voices for OS X, each with its own recognizable speech characteristics (such as gender and age). You can view the list of system voices, and set the default voice, in the Default Voice pane of the Speech system preferences.

If you initialize an NSSpeechSynthesizer instance using the `init` method, the default voice is used. If for some reason you want another voice, initialize the instance with the NSSpeechSynthesizer method `initWithVoice:`. You can change the voice at any time with the `setVoice:` method.

By invoking the class methods `availableVoices` and `defaultVoice`, you can get the list of system voices and the current default voice, respectively. Each voice has multiple attributes, including name, age, gender, and language. By invoking the class method `attributesForVoice:`, you can get an NSDictionary object for a specific voice which contains these attributes. (The argument of this method is a voice identifier, a string of the form `com.apple.speech.synthesis.voice.`_voiceName_.) See the reference documentation for NSSpeechSynthesizer for the valid dictionary keys.

Once you have initialized the NSSpeechSynthesizer object, send the `startSpeakingString:` message to it, passing it the text to speak. Listing 1 illustrates initializing the object with the default voice and then, prior to speaking a string fetched from a text field (`phraseField`), setting the voice as requested by the user in a pop-up list (`voiceList`).

__Listing 1__  Using an NSSpeechSynthesizer object

```objc
- (id)init {
    self = [super init];
    if (self) {
    synth = [[NSSpeechSynthesizer alloc] init]; //start with default voice
                                              //synth is an ivar
    [synth setDelegate:self];
    }
    return self;
}

- (IBAction)speak:(id)sender
{
    NSString *text = [phraseField stringValue];
    NSString *voiceID =[[NSSpeechSynthesizer availableVoices] objectAtIndex:[voiceList indexOfSelectedItem]];
    [synth setVoice:voiceID];
    [synth startSpeakingString:text];
}
```

Note that this code example sets a delegate for the NSSpeechSynthesizer object in the `init` method. NSSpeechSynthesizer defines three methods to allow its delegate to become involved during the speaking of a string of text and after the speaking of a string:

- `speechSynthesizer:willSpeakWord:ofString:`, invoked before each word of the string is spoken, allows the delegate (for example) to visually highlight each word as it is spoken.
- `speechSynthesizer:WillSpeakPhoneme:`, invoked before each phoneme is pronounced, allows the delegate (for example) to animate a mouth pronouncing the phoneme.
- `speechSynthesizer:didFinishSpeaking:` is invoked when the speaking of the string ends. The second parameter of this method indicates whether the text was entirely spoken or was disrupted (as might happen if the user dismisses a spoken alert).

  You might implement this method to adjust the user interface appropriately when speaking ceases. Listing 2 exemplifies one such implementation.

__Listing 2__  An implementation of speechSynthesizer:didFinishSpeaking:

```objc
- (void)speechSynthesizer:(NSSpeechSynthesizer *)sender didFinishSpeaking:(BOOL)finishedSpeaking
{
    [_textToSpeechExampleTextView setSelectedRange:_orgSelectionRange]; // Set selection length to zero.
    [_textToSpeechExampleSpeakButton setTitle:@"Start Speaking"];
    [_saveButton setTitle:@"Save As File..."];
    [_textToSpeechExampleSpeakButton setEnabled:YES];
    [_saveButton setEnabled:YES];
    [_voicePop setEnabled:YES];
}
```

[Next](Recognizing%20Speech.md)[Previous](Introduction%20to%20Speech.md)

