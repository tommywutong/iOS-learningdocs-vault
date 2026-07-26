---
title: 'iPhone Apps I Can''t Have'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/iphone-apps-i-cant-have.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0b1390d65dbd2587'
translated: false
---

> 原文：[iPhone Apps I Can't Have](https://www.mikeash.com/pyblog/iphone-apps-i-cant-have.html)　·　mikeash.com Friday Q&A

Posted at 2010-05-14 02:46 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-05-14: What Every Apple Programmer Should Know](https://www.mikeash.com/pyblog/friday-qa-2010-05-14-what-every-apple-programmer-should-know.html)  
Previous article: [Another Week Without Friday Q&A](https://www.mikeash.com/pyblog/another-week-without-friday-qa.html)  
Tags: [apple](https://www.mikeash.com/pyblog/?tag=apple) [iphone](https://www.mikeash.com/pyblog/?tag=iphone) [rant](https://www.mikeash.com/pyblog/?tag=rant)

iPhone Apps I Can't Have

by [Mike Ash](https://www.mikeash.com/)

**Airfoil**  
 I'm a little biased, of course, since [the company I work for makes it](http://www.rogueamoeba.com/airfoil/mac/), but I'd love to have Airfoil on the iPhone so I can send music directly to an AirPort Express, instead of having to leave my computer turned on and fart around with various substandard remote control solutions. It's impossible to get audio from other apps on the iPhone (even once multitasking happens in 4.0), and apps aren't even allowed to access the audio data in the user's music library. While Airfoil could conceivably be implemented to send audio, there no way for it to get any interesting audio for it to send.

**Hardware brightness control in Kindle**  
 This is a simple one, but also highly desirable. I much prefer Kindle to iBooks on the iPad, because Kindle lacks the distracting visual elements in iBooks, and also has a far superior selection. iBooks does have one nice feature that Kindle lacks: control over the strength of the backlight. Kindle fakes it by adjusting the background color, but it's nowhere near as good. The hardware brightness adjustment is a private API, which third parties like Amazon are prohibited from using. Of course, the rules do not apply to Apple.

**Automatic pasteboard synchronization**  
 I often use my iPhone/iPad at home while also using my Mac, and often want to get data from one to the other. It would be great to have something that would automatically synchronize the pasteboards between them. Currently you can do this by launching a separate app to transfer pasteboard contents, but that's enormously inconvenient compared to a transparent background service. However, launching a separate app is the only option, because Apple doesn't allow us to build a pasteboard sync daemon.

**Text macros**  
 It would be great to have customizable macros that can be inserted into text boxes, either by typing a shortcut or hitting a custom button on the screen. It could be simple stuff like my e-mail address or my phone number, or it could be more complicated stuff like my current latitude and longitude. There's no way for a third party application to manipulate another application like this.

**Alternate keyboards**  
 I use the Dvorak keyboard on my Mac. Although Apple supports Dvorak on the iPad for external hardware keyboards, it's not an option for the on-screen keyboard. While adding a custom layout would probably be a trivial modification, no such activities are allowed.

**Custom input methods**  
 A more generalized version of alternate keyboards, it would be great to be able to load custom input methods that could be accessed in addition to the alternate keyboard. Apple already supplies a method which lets you write Chinese on the screen by drawing the characters with your finger. How about adding one which lets you write English in the same way? Maybe an input method which lets you trace words over a keyboard without lifting your finger, for a speed gain? But again, no such thing is allowed.

**Scripting**  
 I love scripting my computer. I have scripts bound to hotkeys that control my music or upload screenshots to my web site. I have scripts that automatically run backups. I have scripts that take actions when new mail arrives. I build once-off scripts to make different apps work together. Scripting is something that makes a system become far more than just the sum of its parts. Scripting doesn't exist on the iPhone, and is impossible for third parties to add under the current regime.

**Tor/ssh proxy**  
 I go to China every year or two, and when I'm there, I get to enjoy the Great Firewall of China. This means that I can't directly access Facebook, YouTube, and many other sites. Luckily, it's easy to work around the Great Firewall by using services like [Tor](https://www.torproject.org/). This allows me to access the full web, despite being in a country that tries to censor the internet.

(If anyone is getting worried, don't be. The Chinese government doesn't care if a few foreigners bypass their blocks to access information they're able to get in their home country anyway.)

Last time I went to China, I took an iPhone with me and got it up and running with a Chinese carrier, complete with cellular internet access. However, I couldn't access any blocked sites from the iPhone, because tools like Tor simply don't exist there.

Even in the US, it might be nice to keep some activity hidden from AT&T or my local WiFi provider, but there's no nice way to do it.

**Call recorder**  
 While the RAZR I had before I got my iPhone didn't have a lot to recommend it, one nice thing it did have was the ability to record calls. If somebody gave me directions over the phone, I didn't have to scramble for paper, I could just hit a button and record what they said, then transcribe it later at my leisure. I'd love to have this for my iPhone, but third-party apps can't access phone audio, so my only choice is to hope Apple adds it themselves someday.

**WiFi sync**  
 Another nice RAZR feature was the ability to sync contacts and photos with my computer over Bluetooth. I find it wonderfully ironic that my cheap crappy Motorola phone could do wireless sync, but my expensive and enormously powerful iPhone can't. It would be great to have this capability, whether by doing a custom syncing protocol, or just faking out iTunes and making the wireless link look like a USB connection. But again, this can't ever happen, so I'm stuck waiting on Apple to get around to it. In the meantime, my contacts are constantly out of date and it's an annoying ritual to plug my phone into my computer so I can get pictures off of it.

**WiFi hotspot**  
 There are third-party apps that allow you to connect to the internet through your phone with WiFi, but of course none of them are allowed in the store, so they're jailbreak-only. This is a highly desirable capability that's not all that technically difficult, but Apple's loyalty to AT&T is greater than their desire to benefit their customers here.

**WiFi mapper**  
 It would be a bunch of fun to wander around the neighborhood with my phone in my pocket and have it automatically map out all of the networks it came across. Really easy to do from a technical standpoint, but the WiFi APIs are all private, so I'm out of luck.

**Thermal mapper**  
 As some of you may already know, [I fly gliders](https://www.mikeash.com/gliders.html). One of the challenges of glider flight is to map out the location of thermals while climbing. I thought that I could get my iPhone to help with this. By getting vertical velocity information from the GPS chip, and correlating it with horizontal position, I could build a map over time of where the thermal was strongest. Although full three-dimensional velocity data is an inherent output of any GPS calculation, CoreLocation does not provide access to vertical velocity data, only horizontal. And direct access to the GPS chip is forbidden, so I had to give up on my project.

**DOSBox**  
 I have a flight recorder for my glider, which uses GPS to record my position every few seconds so that the flight can later be analyzed (and claimed for a badge or record, if eligible). To dowload the flight record after flying, I have to take the recorder out of the glider, connect it to a PC that we keep at the airport, download the flight, then transfer the record to a flash drive so I can take it home. It's a pain in the ass. The software for downloading the flight is provided by the manufacturer and runs in, yes, DOS. Its computational requirements are low, so it should run reasonably well even in an emulator on a slow ARM chip. It would be great if I could run DOSBox and connect some sort of serial adapter to the iPhone so I could use it to dowload my flights directly, rather than screwing around with keeping a whole PC laptop at the airport. But Apple hates emulators, so this shall never be.

**Location/time based configuration changes**  
 When I'm at home, I want my ringer on. When I'm out walking, I want the phone on vibrate. When I'm flying, I don't want incoming calls at all. I have to make all of these changes manually, even though my phone knows where it is at all times. I don't want audible calendar alerts when I'm at home and my computer will alert me. I want to have it only use a passcode lock if I'm in a place I don't normally visit. It should be able to detect my location and change its configuration to suit. But third-party apps can't change this kind of configuration, so it's impossible to add.

Time-based changes would be interesting as well. I could have the ringer be quieter at night, and loud during the day. I won't bother doing this manually (especially since I don't want to risk forgetting to turn the ringer back up) but it would be great to have the phone do it automatically. I'd also like to have audible new mail alerts during the day, but not at night, and only when I'm at home. But again, it can't be done.

This sort of thing would get even more interesting when combined with scripting. I could have my phone automatically respond to incoming instant messages from people I know to tell them that I'm at the airport and may be slow to respond. My phone could automatically message my wife when I leave for home. It could detect when I'm driving and use voice synthesis to speak incoming messages from certain people I want to be able to hear from on the road. I could set up a reminder to buy cat food that would pop up next time I'm at the store.

**Utilities**  
 So there you have it, 15 apps I'd love to have on my iPhone but that Apple won't let me have, purely for political reasons. Every one of these apps is technically feasible, and many of them not even particularly challenging, but I can't have any of them. They would dramatically increase the utility of my phone, but Apple thinks they know best.

These ideas almost all fall under the category of "utilities". And this is no coincidence: utilities are largely tools which work in concert with other software to offer more power in combination than you get separately. Apple prohibits third party apps from influencing anything outside themselves, so this sort of utility is impossible. The Utilities section of the App Store is a joke. Most of what it contains is either useless or miscategorized, because Apple forbids the creation of any true utility software for this platform.

And so you can see, Apple's restrictions don't just rankle on principle, and don't just hurt me as a developer, but they dramatically reduce the usefulness of the iPhone to me _as a user_. And they dramatically reduce the usefulness of the platform for millions of other users as well, even if they don't know what they're missing.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/iphone-apps-i-cant-have.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
