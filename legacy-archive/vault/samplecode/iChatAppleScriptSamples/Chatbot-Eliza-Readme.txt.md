---
title: iChatAppleScriptSamples
apple_id: DTS10004062
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: InstantMessage
published: '2018-05-03'
source_url: https://developer.apple.com/library/archive/samplecode/iChatAppleScriptSamples/Listings/Chatbot_Eliza_Readme_txt.html
archived_at: '2026-07-18T03:29:33.528889Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iChatAppleScriptSamples](iChatAppleScriptSamples.md)


[Next](Find%20Accounts%20by%20Name-Find%20accounts%20by%20name.applescript.md)[Previous](Chatbot-Eliza-Chatbot-Eliza.pl.md)

# Chatbot-Eliza/Readme.txt

```
Chatbot-Eliza.applescript
v1.0

This script demonstrates an AppleScript "Message Received" handler for iChat. It will take an incoming message and pass it on to Eliza, a virtual psychotherapist, who will then reinterpret the message into a question. The script will take that response and send it back to the originator.

This script requires the installation of the Chatbot-Eliza Perl module, which is available for download at http://search.cpan.org/dist/Chatbot-Eliza/.

This package is currently running with the assumption that Chatbot-Eliza was not installed through CPAN. It uses a file system reference to the library, though if the library has been installed through CPAN it should still work properly. Currently, the script will look for Chatbot-Eliza in a folder on your desktop named Chatbot-Eliza-1.04.

To install:

1. Copy the files "ChatbotEliza.applescript" and "ChatbotEliza.pl" to ~/Library/Scripts/iChat.

2. Install Chatbot-Eliza. You can either install the library using CPAN, or you can unzip the package and place the unzipped folder on your desktop.

3. Open ChatbotEliza.applescript and configure the path to the elizaScriptDir if necessary.

4. Test run the script.

5. Set the handler up in iChat by opening Preferences and going to Alerts.

6. For the event "Message Received," check the box for "Run AppleScript" and select "Chatbot-Eliza" from the dropdown.

7. Repeat for the "Text Invitation" event.
```

[Next](Find%20Accounts%20by%20Name-Find%20accounts%20by%20name.applescript.md)[Previous](Chatbot-Eliza-Chatbot-Eliza.pl.md)

