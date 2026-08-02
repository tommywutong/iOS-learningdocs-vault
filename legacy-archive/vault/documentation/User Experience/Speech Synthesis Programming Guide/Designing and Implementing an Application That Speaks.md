---
title: Speech Synthesis Programming Guide
apple_id: TP40004365
resource_type: Guide
platform: macOS
topic: User Experience
technology: ApplicationServices
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SpeechSynthesisProgrammingGuide/UsingSpeech/UsingSpeech.html
archived_at: '2026-07-18T02:12:51.874385Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Speech Synthesis Programming Guide](Introduction%20to%20Speech%20Synthesis%20Programming%20Guide.md)


[Next](Techniques%20for%20Customizing%20Synthesized%20Speech.md)[Previous](Speech%20Synthesis%20in%20OS%20X.md)

# Designing and Implementing an Application That Speaks

This chapter gathers together some strategies to consider and guidelines to follow as you design (or retrofit) an application to produce spoken output. It begins with a survey of different implementation strategies you should consider to find the one that meets your goals. It then provides user-interface guidelines you should keep in mind as you design your application. Finally, this chapter outlines the speech synthesis APIs available to you and provides some examples that show how to get started.

Spoken output is a natural enhancement for a broad range of applications, from games to productivity applications to educational applications. For example, if you’re designing an application for language-learning, it’s clear you need to provide accurately pronounced speech users can emulate. If you’re developing a game, you probably want to provide a large set of expressive phrases your characters can speak. But synthesized speech can also enhance an application that doesn’t have such obvious reasons to produce spoken output, because it can provide users with a more convenient and more enjoyable way to interact with the application.

As you design your application, look for ways synthesized speech can enhance the user interface. A few suggestions are included in [User Interface Design Guidelines for Speech](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnbnknltg). The following sections describe ways you can use synthesized speech in your application, divided into three categories that roughly correspond to the levels of effort required to implement them.

Even if you do not include any speech-specific code in your application, users will be able to hear most of the text displayed in your application spoken aloud by a system voice. In the Text to Speech pane of Speech preferences, users can create a key combination to use when they want to hear the text they’ve selected in any application. In the same preference pane, users can also choose to hear the text of alerts spoken aloud (this is a feature known as Talking Alerts) and to be told when an application requires attention.

You do not have to do anything special to allow your users to benefit from these features; to the contrary, if you use standard, system-supplied APIs and technologies, it comes for free. Selectable text that appears in your application, including user-supplied text, can be spoken aloud when users press their designated key combination or when they select Speech > Start Speaking Text from the Services menu item. (Note that the Services menu item is included by default in Cocoa and Carbon applications; for more information, see _[Services Implementation Guide](../../Cocoa/Services%20Implementation%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydc2i)_ and _[Setting Up Your Carbon Application to Use the Services Menu](../../Carbon/Setting%20Up%20Your%20Carbon%20Application%20to%20Use%20the%20Services%20Menu/Introduction%20to%20Setting%20Up%20Your%20Carbon%20Application%20to%20Use%20the%20Services%20Menu.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojt)_.) When your application uses system-provided mechanisms for displaying alerts, the Talking Alerts feature automatically speaks the alert text.

You may find that these built-in features meet your application’s speech needs. If, however, you want to enhance and customize the spoken output in your application to differentiate it from competing products, read the following sections to explore ways you can do this.

In addition to allowing users to select text to hear spoken aloud, your application can speak when it encounters specific conditions or performs specific tasks. For example, your application could guide new users by describing the steps required to accomplish common tasks. The speech synthesis APIs provide functions and methods you can use to associate spoken output with application-specific tasks and events (for more information on how to do this, see [Synchronize Speech with Application-Specific Actions](Techniques%20for%20Customizing%20Synthesized%20Speech.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknlts)).

If you want to have more control over the production of speech in your application, you can override some of the default behaviors of the synthesizer. One way to do this is to use Carbon speech synthesis functions to change speech-channel attributes, such as speech rate and pitch. Another way to do this is to use embedded speech commands (described in [Control Speech Quality Using Embedded Speech Commands](Speech%20Synthesis%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqmznknltk)) and insert them as needed in the text to be spoken. The synthesizer uses these commands to alter the intonation of words and phrases by controlling the pitch, word emphasis, and pause length, among other attributes. This technique is especially useful if you want ensure the correct pronunciation of a proper noun (such as your company name) or if the spoken content must conform to specific requirements (such as in a language-learning application or other educational software). Embedded speech commands are available regardless of the programming language you’re using.

The phonemic and TUNE input-processing modes allow you to make fine-grained adjustments to spoken output. For example, you can stipulate the pronunciation of a word by giving the synthesizer the individual phonemes that comprise the word.

Using the TUNE input-processing mode, you can reproduce all the minute variations in pitch and rate of an actual utterance, allowing your application to produce speech that replicates some of the subtleties of human speech. If you want your application to produce speech that follows such exact specifications, see [Use Phoneme Modifiers to Adjust Pronunciation](Techniques%20for%20Customizing%20Synthesized%20Speech.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknlti) and [Use the TUNE Format to Supply Complex Pitch Contours](Techniques%20for%20Customizing%20Synthesized%20Speech.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknlto).

As described in [Why Use Synthesized Speech?](Speech%20Synthesis%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqmznknltcma), there are many ways to enhance your application by providing spoken output. For example, you can use speech to notify users of something that happened in the background, such as “Your download is finished” or “You have a meeting in 15 minutes.“ Essentially, spoken output is another facet of the user interface and, as such, it should follow most of the high-level guidelines in _OS X Human Interface Guidelines_. In addition to those guidelines, keep in mind this section’s design considerations and speech-specific guidelines as you design your application.

Consider providing spoken confirmation of information users enter or selections they make. For example, a user may not be looking at the screen when typing in data from another source, and spoken confirmation of the input would be welcome. Similarly, if a user inadvertently selects the wrong item from a long list, spoken confirmation of each choice would immediately alert the user to any mistakes.

When using speech to notify users that an event has occurred, consider pausing for a few seconds between the visual display of the event (such as a dialog) and the spoken message. Speech is an effective way to get users’s attention if they are not already looking at the screen, but if they are, the spoken notification might seem redundant. Inserting a delay between the visual and aural notification gives users the opportunity to respond to the event without hearing any speech. If such a pause makes sense in your application, be sure to provide a way for users to customize its length.

To provide a consistent and enjoyable speech experience to your users, follow these guidelines:

- Provide a way for users to turn on and off the spoken output your application produces. Hearing-impaired users will not benefit from the speech your application generates, and other users may not like it or may use your application in situations that require silence (such as in a library). Consider your target market carefully before you decide to make speech the default setting.
- Be sure to provide a visual alternative to all spoken (or aural) communication your application produces. Users should be able to choose between spoken and visual communication without losing access to any information or functionality.
- As much as possible, provide ways for users to customize the speech they hear. For example, users should be able to choose a pleasing voice and to set the speech rate and pitch to comfortable levels.
- When testing your application, be sure to listen to all spoken output your application generates. This way, you’ll be able to catch incorrect and ambiguous pronunciations and fix them with embedded speech commands and phoneme modifiers.
- As with written alerts, spoken alerts should tell the user what happened, why it happened, and what the user can do about it. For more guidelines on writing effective alert messages, see _OS X Human Interface Guidelines_.
- As much as possible, express complicated ideas in a few short sentences instead of one long sentence. It’s much harder for users to process complicated spoken information because they can’t go back and reread the parts they missed or didn’t understand. Effective use of punctuation can also help make complex sentences easier to understand. This is because the synthesizer, like a human speaker, pauses when it encounters commas, semicolons, and periods. For more information on how to draw users’s attention to the important information within a sentence, see [Four Ways to Improve Spoken Output](Techniques%20for%20Customizing%20Synthesized%20Speech.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknlte).
- Be sure to document the speech capabilities of your application. If users don’t know what features are available and how they can customize them, they might not ever use them.

Before you begin designing your application with synthesized speech in mind, note that the type of customization you plan to do has some impact on your choice of API. Both Carbon and Cocoa supply basic speech-synthesis functionality, but the Carbon API provides more programmatic control over speech attributes. Unlike the Carbon speech synthesis API, the `NSSpeechSynthesizer` class defined in the Application Kit does not support the ability to convert text to phonemes or to change speech attributes. If you don’t plan to take advantage of the programmatic features now or in a future version of your application, you can use the Cocoa API without worrying about having to redesign and recode the application later. If, however, you want to support advanced capabilities (or there’s a chance that you might do so in the future), you should consider using the Carbon API from the beginning.

Although you can mix the Cocoa and Carbon speech synthesis APIs in a single application, you may experience a few difficulties because of differences in implementation. For example, if you specify a voice that the current speech synthesizer doesn’t support, in Carbon you must explicitly close the current speech channel and open a new one to use the new voice, whereas in Cocoa this process is automatic. You may find that your best option is to develop the application in Cocoa, but use the Carbon speech synthesis API for all speech-related tasks.

Before you choose an API, bear in mind that you can accomplish a great deal of speech customization by adding embedded commands to the text your application passes to the synthesizer. However, a potential disadvantage to using embedded commands is that you must add the appropriate embedded commands to every occurrence of a particular word to specify its pronunciation. Contrast this with calling a function that sets a speech attribute for all spoken output that passes through a speech channel. Depending on your circumstances, however, you may decide that this disadvantage is outweighed by the finer-grained control that comes with using embedded commands.

The remainder of this section provides brief overviews of the Cocoa and Carbon speech synthesis APIs. For in-depth reference information on these APIs, see _[NSSpeechSynthesizer Class Reference](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer)_ and _[Speech Synthesis Manager Reference](https://developer.apple.com/documentation/applicationservices/speech_synthesis_manager)_.

The Cocoa API includes the [NSSpeechSynthesizer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer) class, which handles a number of speech synthesis tasks in a way native to Objective-C. When you create and initialize an instance of `NSSpeechSynthesizer`, a speech channel is created and a voice (either the default system voice or one you designate in the initialization method) is associated with the object. The `NSSpeechSynthesizer` object is your application’s conduit to the Speech Synthesis framework.

The `NSSpeechSynthesizer` class defines methods that allow you to:

- Get information about a voice (such as age and gender)
- Change the voice used for spoken output
- Determine if another application is currently speaking
- Start and stop speech
- Manage delegates

To make your application speak a word or phrase, you use an instance method to send text to your `NSSpeechSynthesizer` object (alternatively, you can use an instance method to cause the sound output to be saved to a file). Using the delegate methods defined by the `NSSpeechSynthesizer` class, you can also perform application-specific actions just before a word or phoneme is spoken or just after the synthesizer finishes speaking a string. You might use these methods to, for example, change the state of a start/stop speaking button or to synchronize the animation of a character’s mouth with the spoken output.

Although you can use a class method to get the attributes for a specific voice, the `NSSpeechSynthesizer` class does not define methods that allow you to get or change the attributes of a speech channel. In addition, the `NSSpeechSynthesizer` class does not support the programmatic conversion of text to phonemes. To do these things, you must use functions in the Carbon speech synthesis API.

The Carbon speech synthesis API (also called the Speech Synthesis Manager) includes functions that allow you to:

- Create and manage speech channels
- Adjust speech attributes on a speech channel
- Convert text to phonemes
- Get information about speech channels and voices
- Start, stop, and pause speech
- Create, invoke, and dispose of universal procedure pointers that point to functions you supply to synchronize speech with application-specific actions

In addition to these functions, the Carbon speech synthesis API defines constants that describe voice and speech-channel attributes, data types (such as phoneme and voice description structures), and a large number of selectors that operate on speech channels.

Even though the Carbon speech synthesis API is not object-oriented, it may help to think of a speech channel (a structure of type [SpeechChannel](https://developer.apple.com/documentation/applicationservices/speechchannel)) as analogous to an instance of the `NSSpeechSynthesizer` class. This is because a speech channel is the primary conduit between your application and the Speech Synthesis framework, and you must create one to perform most speech-related tasks, such as getting information about a voice, sending text to be spoken, or adjusting speech attributes. The one exception to this is the [SpeakString](https://developer.apple.com/documentation/applicationservices/1552250-speakstring) function, which does not require you to create a speech channel. When you pass a string to the `SpeakString` function, the Speech Synthesis Manager automatically creates and manages the structures required to speak.

Using selectors that you can pass to the [SetSpeechInfo](https://developer.apple.com/documentation/applicationservices/1552223-setspeechinfo) function, you can replicate some of the functionality you get when you use embedded speech commands. For example, you can change the input-processing mode on the speech channel by passing the `soInputMode` selector. This has the same effect as the `[[inpt <mode>]]` embedded speech command, except that it operates on the speech channel as a whole, not on a portion of the text. [Table 3-1](Techniques%20for%20Customizing%20Synthesized%20Speech.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknltm) pairs each embedded speech command with its analogous selector, if one exists. Other selectors allow you to set speech channel attributes or to associate a callback function with a speech channel. See _[Speech Synthesis Manager Reference](https://developer.apple.com/documentation/applicationservices/speech_synthesis_manager)_ for a complete list of available selectors.

This section describes how to use the Cocoa and Carbon APIs to perform basic set-up tasks, such as getting a speech channel, designating a specific voice, starting and stopping speech, and responding to speech events.

To generate speech using the Cocoa speech synthesis API, you must instantiate an `NSSpeechSynthesizer` object and send to it the text to speak. The code in Listing 2-1 shows how to use this object to get information about available voices and how to respond to some speech events. This code is a simplified version of the NSSpeechSynthesizerExample example project located in `/Developer/Examples/Speech/Synthesis`. The code in Listing 2-1 does not show how to create a pop-up menu of available voices or manage text selection and it does not implement any error handling.

The code in Listing 2-1 shows an implementation of an `NSObject` subclass called `ExampleWindow`. It uses a simple window that contains the following items:

- A text view (declared as `NSTextView * _textView`) that displays the text to be spoken
- A pop-up menu (declared as `NSPopUpButton * _voicePop`) that displays the available voices from which the user can choose
- A button (declared as `NSButton * _speakButton`) the user clicks to start and stop speech

__Listing 2-1__  Generating speech using the Cocoa speech synthesis API

```objc
@implementation ExampleWindow
/* Instantiate an NSSpeechSynthesizer object when the application starts */
- (void)awakeFromNib
{
    _speechSynthesizer  = [NSSpeechSynthesizer new];
    /* Make the ExampleWindow object the responder to NSSpeechSynthesizer delegate methods */
    [_speechSynthesizer setDelegate:self];

    /* Call a custom method to populate the pop-up menu of available voices (implementation not shown) */
    [self getSpeechVoices];
}

/* When the user clicks the Start Speaking button, invoke the custom startSpeakingTextView method to retrieve (or create) the text and speak it */
- (IBAction) speakTextButtonSelected:(id)sender
{
  [self startSpeakingTextView];
}

- (void)startSpeakingTextView
{
    if([_speechSynthesizer isSpeaking]) {
        [_speechSynthesizer stopSpeaking];
    }
    else {
         NSString *    theViewText;
        /* If the user chooses to hear the default system voice, get the text to speak from the window (either the default text or user-supplied) */
        if ([_voicePop indexOfSelectedItem] == 0) {
            [_speechSynthesizer setVoice:NULL];
            theViewText = [_textView string];
        }
        /* Otherwise, get the user's chosen voice, create a string using the voice's demo text, and speak it */
        else {
            [_speechSynthesizer setVoice:[[NSSpeechSynthesizer availableVoices] objectAtIndex:[_voicePop indexOfSelectedItem] - kNumOfFixedMenuItemsInVoicePopup]];
            /* Get the attributes of the chosen voice */
            NSDictionary * attributes = [NSSpeechSynthesizer attributesForVoice:[_speechSynthesizer voice]];
            /* Get the value of the voice's name attribute */
            NSString * theName = [attributes objectForKey:NSVoiceName];
            /* Build a string using the voice's name and demo text in this format: "This is <name>. <Demo text.>" */
            theViewText = [NSString stringWithFormat:@"This is %@. %@", theName,[attributes objectForKey:NSVoiceDemoText]];
            /* Display this new string in the window */
            [_textView setString:theViewText];
         }
        /* Send string to synthesizer object */
        [_speechSynthesizer startSpeakingString:theViewText];
        /* Change button name to reflect current state */
        [_speakButton setTitle:@"Stop Speaking"];
    }
}
@end
```

As shown in the `awakeFromNib` method in Listing 2-1, the `ExampleWindow` object will respond to delegate methods defined by the `NSSpeechSynthesizer` class. Listing 2-2 includes example implementations of two of these methods, showing how to perform application-specific actions that are synchronized with speech events.

__Listing 2-2__  Using delegate methods to respond to speech events

```objc
/* This delegate method is invoked when the NSSpeechSynthesizer object has finished speaking. This happens when there is no more text to speak or when the user clicks the Stop Speaking button. */

- (void)speechSynthesizer:(NSSpeechSynthesizer *)sender didFinishSpeaking:(BOOL)finishedSpeaking
{
    /* Return cursor to beginning of line */
    [_textView setSelectedRange:NSMakeRange(0,0)];
    /* Reset button title to initial string */
    [_speakButton setTitle:@"Start Speaking")];
    [_speakButton setEnabled:YES];
    [_voicePop setEnabled:YES];
}

/* This delegate method is called when a word (defined by its character range within the string) is about to be spoken. This implementation uses this information to highlight each word as it's being spoken. */

- (void)speechSynthesizer:(NSSpeechSynthesizer *)sender willSpeakWord:(NSRange)characterRange ofString:(NSString *)string
{
    UInt32    selectionPosition = characterRange.location;
    UInt32    wordLength = characterRange.length;

    [_textView scrollRangeToVisible:NSMakeRange(selectionPosition, wordLength)];
    /* Highlight word about to be spoken */
    [_textView setSelectedRange:NSMakeRange(selectionPosition, wordLength)];
    [_textView display];
}
```


To generate speech using the Carbon speech synthesis API, you must create a speech channel and send to it the text to speak. The example code in this section is modeled on the CocoaSpeechSynthesisExample example project (located in `/Developer/Examples/Speech/Synthesis`), which shows how to use the Carbon speech synthesis API within a Cocoa application. Much of the example application’s infrastructure is provided by Cocoa’s [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) class and the code that displays and manages the window and its contents is not reproduced in the following code listings. The code in the listings below shows how to use a handful of the Carbon speech synthesis functions; see the CocoaSpeechSynthesisExample application for a broader sampling.

The code in Listing 2-3 shows a partial implementation of an `NSDocument` subclass, called `SpeakingTextWindow`. `SpeakingWindow` contains the following instance variables:

- `fCurSpeechChannel` (of type `SpeechChannel`) to point to the current speech channel
- `fCurrentlySpeaking` (of type `BOOL`) to indicate the current speech state

__Listing 2-3__  Generating speech using the Carbon speech synthesis API

```objc
/* Callback function prototype: */
static pascal void     MyWordCallBackProc(SpeechChannel inSpeechChannel, long inRefCon, long inWordPos, short inWordLen);

@implementation SpeakingTextWindow
- (void)awakeFromNib
{
    OSErr        theErr = noErr;
    short        numOfVoices;
    long         voiceIndex;
    BOOL        voiceFoundAndSelected = false;
    VoiceSpec    theVoiceSpec; /* VoiceSpec is a structure that contains the identity of the synthesizer required to use a voice and the ID of a voice. */

    /* Get the number of voices on the system. Note that you do not need to get a speech channel to get information about available voices. */
    theErr = CountVoices(&numOfVoices); // Handle error if necessary.

    for (voiceIndex = 1; voiceIndex <= numOfVoices; voiceIndex++) {
        VoiceDescription    theVoiceDesc;
        /* Get the VoiceSpec structure for this voice. The structure fields will be filled in by a call to GetVoiceDescription. */
        theErr = GetIndVoice(voiceIndex, &theVoiceSpec); // Handle error if necessary.

        /* Fill in the fields of the theVoiceDesc VoiceDescription structure. */
        theErr = GetVoiceDescription(&theVoiceSpec, &theVoiceDesc, sizeof(theVoiceDesc)); // Handle error if necessary.

        /* Add this voice name to the pop-up menu (not shown). */
    }

    /* If a speech channel already exists, dispose of it. */
    if (fCurSpeechChannel) {
        theErr = DisposeSpeechChannel(fCurSpeechChannel); // Handle error if necessary.
        fCurSpeechChannel = NULL;
    }

    /* Create a speech channel. */
    theErr = NewSpeechChannel(NULL, &fCurSpeechChannel); // Handle error if necessary.
    /* Set the refcon to the document controller object to ensure that the callback functions have access to it. */
    theErr = SetSpeechInfo(fCurSpeechChannel, soRefCon, (Ptr)self); // Handle error if necessary.
    /* Enable the Start/Stop and Pause/Continue buttons (not shown). */
}

- (IBAction)startStopButtonPressed:(id)sender
{
    /* This action method is called when a user clicks the Start/Stop speaking button. */
    OSErr theErr = noErr;

    if (fCurrentlySpeaking) {
        /* If speech is currently being produced, stop it immediately. Alternatively, you could use the StopSpeechAt function to stop the speech at the end of a word or sentence.*/
        theErr = StopSpeech(fCurSpeechChannel); // Handle error if necessary.
        fCurrentlySpeaking = false;
        /* Update the controls, based on current speaking state (the updateSpeakingControlState method is not shown). */
        [self updateSpeakingControlState];
    }
    else {
        /* Call the method that sets up the callbacks on the speech channel and sends the text to be spoken. */
        [self startSpeakingTextView];
    }
}

- (void)startSpeakingTextView
{
    /* This method sets up a callback that gets called when a word has been spoken. It also starts spoken output by calling the SpeakText function. */
    OSErr theErr = noErr;
    NSString * theViewText;

    /* Get the text from the window and store in theViewText (not shown). */
    /* Set up the word callback function. Other callback functions can be set up in a similar way. */
    theErr = SetSpeechInfo(fCurSpeechChannel, soSpeechDoneCallBack, MySpeechDoneCallBackProc); // Handle error if necessary.

    /* Convert the theViewText NSString object to a C string variable.*/
    char * theTextToSpeak = (char *)[theViewText lossyCString];

    /* Send the text to the speech channel. */
    theErr = SpeakText(fCurSpeechChannel, theTextToSpeak, strlen(theTextToSpeak)); // Handle error if necessary.

    /* Update variables and control states (you might want to define other variables to hold the current pause state and the most recent error code). */
    fCurrentlySpeaking = true;
    [self updateSpeakingControlState];
}
```

As shown in Listing 2-3, the `startSpeakingTextView` method sets up a callback procedure on the speech channel. The CocoaSpeechSynthesisExample example application uses the callback procedure to call a function that highlights each word in the text as it’s spoken.

The code in Listing 2-4 shows the callback procedure, which uses the `NSObject` method [performSelectorOnMainThread:withObject:waitUntilDone:](https://developer.apple.com/documentation/objectivec/nsobject/1414900-performselector) to call the routine that actually performs the processing associated with the callback. The reason `MyWordCallBackProc` doesn’t perform the word highlighting itself is that all Carbon speech synthesis callbacks (except [SpeechTextDoneProcPtr](https://developer.apple.com/documentation/applicationservices/speechtextdoneprocptr)) call their associated functions on a thread other than the main thread. Unless you’ve indicated that your Cocoa application is multithreaded, this can cause problems if your callback routine touches the user interface or other application objects. To avoid these problems, use the `performSelectorOnMainThread:withObject:waitUntilDone:` method to ensure your callback processing routine is called on the main thread. Of course, this mechanism is unnecessary in a pure Carbon application.

__Listing 2-4__  Using a Carbon callback procedure to respond to a speech event

```
pascal void MyWordCallBackProc(SpeechChannel inSpeechChannel, long inRefCon, long inWordPos, short inWordLen)
{
    NSAutoreleasePool *    pool = [[NSAutoreleasePool alloc] init];

    /* Call the highlightWordWithParams: method to highlight each word as it's spoken. highlightWordWithParams (not shown) receives a dictionary containing two values: the number of bytes between the beginning of the text and the beginning of the word about to be spoken and the length in bytes of that word. */

    [(SpeakingTextWindow *)inRefCon performSelectorOnMainThread:@selector(highlightWordWithParams:) withObject:[NSDictionary dictionaryWithObjectsAndKeys:[NSNumber numberWithLong:inWordPos], kWordCallbackParamPosition, [NSNumber numberWithLong:inWordLen], kWordCallbackParamLength, NULL] waitUntilDone:false];
    [pool release];
}
```

If you’d like to explore making your Cocoa application multithreaded, see _[Threading Programming Guide](../../Cocoa/Threading%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2i)_. If you’re writing an application similar to CocoaSpeechSynthesisExample and you’d like to make it multithreaded, be sure to include the following line of code before you call any Carbon speech synthesis function for the first time:

```
[NSThread detachNewThreadSelector:@selector(self) toTarget:self withObject:nil];
```

After you’ve used the [detachNewThreadSelector:toTarget:withObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/clm/NSThread/detachNewThreadSelector:toTarget:withObject:) method to create a new thread, you can then perform the callback processing tasks within your callback procedures.

Using the AppleScript `say` command, you can cause text to be spoken aloud or saved to a file. The `say` command is one of the user interaction commands available in the Standard Additions scripting addition (available in `/System/Library/ScriptingAdditions`). To experiment with the script examples in this section, open the Script Editor application (located in `Applications/AppleScript`), type the script into the Script Editor window, and click Run.

The `say` command speaks the string that follows it (the string can be text enclosed in double quotes or text in a variable). Optionally, you can use the `using` parameter to tell the `say` command to use a specific voice and the `saving to` parameter to redirect the spoken output to an AIFF file. The `say` command also accepts two parameters that are ignored unless Speech Recognition is turned on. These two parameters (`displaying` and `waiting until completion`) are not described in this document. For more information on the syntax and usage of the `say` command, open `StandardAddition.osax` in Script Editor.

The following example uses the Switch to Finder script (located in `Applications/AppleScript/Example Scripts/Finder Scripts`) to show how you can add the `say` command to a script to produce spoken output.

__Listing 2-5__  Using AppleScript to produce spoken output

```
tell application "Finder"     activate     set visible of every process whose visible is true and name is not "Finder" to false     say "To see other application windows again, select Show All from the Finder menu." using "Vicki" end tell
```

If you save the spoken output to an AIFF file, you can use it in some other application or listen to it in iTunes (or download it to an iPod). The following example adds a second `say` command to the script in Listing 2-5, this one directing some of the spoken output to a file in the `/Users` folder.

__Listing 2-6__  Using AppleScript to save spoken output to a file

```
tell application "Finder"     activate     set visible of every process whose visible is true and name is not "Finder" to false     say "To see other application windows again, select Show All from the Finder menu." using "Vicki"     say "This is an example of using the AppleScript say command to save spoken output to a file." saving to "Users:AppleScript_speech.aiff" end tell
```

[Next](Techniques%20for%20Customizing%20Synthesized%20Speech.md)[Previous](Speech%20Synthesis%20in%20OS%20X.md)

