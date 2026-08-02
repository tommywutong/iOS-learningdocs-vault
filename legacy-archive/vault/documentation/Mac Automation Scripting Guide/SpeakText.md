---
title: Mac Automation Scripting Guide
apple_id: TP40016239
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/SpeakText.html
archived_at: '2026-07-15T07:46:17.692464Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Mac Automation Scripting Guide](index.md)



## Speaking Text

Spoken text is another way to provide feedback to users during script execution; instead of reading a message visually, the user can listen to it audibly. Listing 25-1 and Listing 25-2 show how the Standard Additions scripting addition’s `say` command can be used to speak a phrase.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=say%20%22Processing%20is%20complete.%22)

__Listing 25-1__AppleScript: Speaking text

1. `say "Processing is complete."`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20app%20%3D%20Application.currentApplication%28%29%0Aapp.includeStandardAdditions%20%3D%20true%0A%0Aapp.say%28%22Processing%20is%20complete.%22%29)

__Listing 25-2__JavaScript: Speaking text

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
4. `app.say("Processing is complete.")`

The `say` command has a number of optional parameters, some of which allow you to specify a voice and attributes such as speaking rate, pitch, and modulation. See Listing 25-3 and Listing 25-4.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=say%20%22Just%20what%20do%20you%20think%20you%27re%20doing%20Dave%3F%22%20using%20%22Alex%22%20speaking%20rate%20140%20pitch%2042%20modulation%2060)

__Listing 25-3__AppleScript: Speaking text with custom speech attributes

1. `say "Just what do you think you're doing Dave?" using "Alex" speaking rate 140 pitch 42 modulation 60`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20app%20%3D%20Application.currentApplication%28%29%0Aapp.includeStandardAdditions%20%3D%20true%0A%0Aapp.say%28%22Just%20what%20do%20you%20think%20you%27re%20doing%20Dave%3F%22%2C%20%7B%0A%20%20%20%20using%3A%20%22Alex%22%2C%0A%20%20%20%20speakingRate%3A%20140%2C%0A%20%20%20%20pitch%3A%2042%2C%0A%20%20%20%20modulation%3A%2060%0A%7D%29%0A)

__Listing 25-4__JavaScript: Speaking text with custom speech attributes

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
4. `app.say("Just what do you think you're doing Dave?", {`
5. `using: "Alex",`
6. `speakingRate: 140,`
7. `pitch: 42,`
8. `modulation: 60`
9. `})`

### Saving Text as an Audio File

The `say` command’s `saving as` parameter adds another level of power, enabling text to be converted to audio format and saved as an `.aiff` file for later listening. This technique could be used, for example, to save email messages in audio format, as demonstrated by Listing 25-5 and Listing 25-6.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=tell%20application%20%22Mail%22%0A%20%20%20%20tell%20message%201%20of%20inbox%0A%20%20%20%20%20%20%20%20set%20theSubject%20to%20subject%0A%20%20%20%20%20%20%20%20set%20theBody%20to%20content%0A%20%20%20%20end%20tell%0Aend%20tell%0A%0Aset%20theOutputFile%20to%20%28path%20to%20desktop%20as%20string%29%20%26%20%22message.aiff%22%0Aset%20theAudio%20to%20%22Message%20Subject%3A%20%22%20%26%20theSubject%20%26%20return%20%26%20%22Body%3A%20%22%20%26%20theBody%0Asay%20theAudio%20saving%20to%20theOutputFile)

__Listing 25-5__AppleScript: Saving text as audio

1. `tell application "Mail"`
2. `tell message 1 of inbox`
3. `set theSubject to subject`
4. `set theBody to content`
5. `end tell`
6. `end tell`
8. `set theOutputFile to (path to desktop as string) & "message.aiff"`
9. `set theAudio to "Message Subject: " & theSubject & return & "Body: " & theBody`
10. `say theAudio saving to theOutputFile`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20Mail%20%3D%20Application%28%22Mail%22%29%0Avar%20app%20%3D%20Application.currentApplication%28%29%0Aapp.includeStandardAdditions%20%3D%20true%0A%0Amessage%20%3D%20Mail.inbox.messages%5B0%5D%0Asubject%20%3D%20message.subject%28%29%0Abody%20%3D%20message.content%28%29%0A%0AoutputFile%20%3D%20%28%28app.pathTo%28%22desktop%22%29.toString%28%29%29%20%2B%20%22%2Fmessage.aiff%22%29%0Aaudio%20%3D%20%22Message%20Subject%3A%20%22%20%2B%20subject%20%2B%20%22%5CnBody%3A%20%22%20%2B%20body%0Aapp.say%28audio%2C%20%7BsavingTo%3A%20outputFile%7D%29)

__Listing 25-6__JavaScript: Saving text as audio

1. `var Mail = Application("Mail")`
2. `var app = Application.currentApplication()`
3. `app.includeStandardAdditions = true`
5. `message = Mail.inbox.messages[0]`
6. `subject = message.subject()`
7. `body = message.content()`
9. `outputFile = ((app.pathTo("desktop").toString()) + "/message.aiff")`
10. `audio = "Message Subject: " + subject + "\nBody: " + body`
11. `app.say(audio, {savingTo: outputFile})`

### Speaking Text While Displaying a Dialog

Typically, a script executes a single command at a time, waiting for a command to complete before moving onto the next. Listing 25-7 and Listing 25-8 demonstrate how to display a dialog message, while simultaneously using the `NSTask` class in the Foundation framework to read the message out loud.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=use%20framework%20%22Foundation%22%0Ause%20scripting%20additions%0A%0Aset%20theStatusText%20to%20%22Processing%20is%20complete.%22%0Aset%20theTask%20to%20%28current%20application%27s%20NSTask%27s%20launchedTaskWithLaunchPath%3A%22%2Fusr%2Fbin%2Fsay%22%20arguments%3A%7BtheStatusText%7D%29%0Atry%0A%20%20%20%20display%20dialog%20theStatusText%0A%20%20%20%20theTask%27s%20terminate%28%29%0Aon%20error%0A%20%20%20%20try%0A%20%20%20%20%20%20%20%20theTask%27s%20terminate%28%29%0A%20%20%20%20end%20try%0Aend%20try)

__Listing 25-7__AppleScriptObjC: Speaking text while displaying a dialog

1. `use framework "Foundation"`
2. `use scripting additions`
4. `set theStatusText to "Processing is complete."`
5. `set theTask to (current application's NSTask's launchedTaskWithLaunchPath:"/usr/bin/say" arguments:{theStatusText})`
6. `try`
7. `display dialog theStatusText`
8. `theTask's terminate()`
9. `on error`
10. `try`
11. `theTask's terminate()`
12. `end try`
13. `end try`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20app%20%3D%20Application.currentApplication%28%29%0Aapp.includeStandardAdditions%20%3D%20true%0A%0Avar%20statusText%20%3D%20%22Processing%20is%20complete.%22%0Avar%20task%20%3D%20%24.NSTask.launchedTaskWithLaunchPathArguments%28%22%2Fusr%2Fbin%2Fsay%22%2C%20%5BstatusText%5D%29%0A%0Atry%20%7B%0A%20%20%20%20app.displayDialog%28statusText%29%0A%20%20%20%20task.terminate%0A%7D%0Acatch%28error%29%7B%0A%20%20%20%20task.terminate%0A%7D)

__Listing 25-8__JavaScriptObjC: Speaking text while displaying a dialog

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
4. `var statusText = "Processing is complete."`
5. `var task = $.NSTask.launchedTaskWithLaunchPathArguments("/usr/bin/say", [statusText])`
7. `try {`
8. `app.displayDialog(statusText)`
9. `task.terminate`
10. `}`
11. `catch(error){`
12. `task.terminate`
13. `}`

[Displaying Notifications](DisplayNotifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnrrfvjvomi)

[Prompting for Files or Folders](PromptforaFileorFolder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqobrfvjvomi)
