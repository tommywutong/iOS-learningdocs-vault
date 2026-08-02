---
title: DMFkey Source
apple_id: DTS10000436
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/DMFkey_Source/Introduction/Intro.html
archived_at: '2026-07-18T03:05:48.982963Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](DMFkey.c.md)

# DMFkey Source

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon Display Manager (either 1.2 or 2.x). This means running either System 7.1.2 through 7.5.1 for Display Manager 1.2 features, or 7.5.2 and later or Display Enabler 2.0 to get Display Manager 2.0 features. |

DMFkey (short for Display Manager Flip FKey) is a sample which makes use of the RequestVideo sample code API. For information about the RequestVideo sample source code, please refer to the Read Me file for the PlayVideo sample code. Display Flip FKey is another example of Display Manager sample code, this time with an FKey wrapper. It uses the cool new Display Manager 2.0 to change the monitor screen resolution the specified HxV resolutions. This FKey will flip between 640x480 and BIG. BIG is up to 2000x2000 if your monitor supports it. Display Flip FKey requires that the Display Manager (either 1.2 or 2.x) be present in your system. This means running either System 7.1.2 through 7.5.1 for Display Manager 1.2 features, or 7.5.2 and later or Display Enabler 2.0 to get Display Manager 2.0 features. Installing It Into The System : The Display Flip FKey uses the best way to install FKey's into the system - it is packaged as a font suitcase. Just drop the Display Flip FKey suitcase into your system's Fonts folder of your system and off you go - it is ready to run. The only drawback is, like all things in the system Fonts folder, only the Finder can be running when you want to take things out if it. This means quitting all your normally open applications like Malph, Darkside, and CodeWarrior before you can remove the Display Flip FKey. You can change the FKey number by changing the resource ID of the FKey either in the project or using ResEdit after the fact. Requirements: Display Manager (either 1.2 or 2.x). This means running either System 7.1.2 through 7.5.1 for Display Manager 1.2 features, or 7.5.2 and later or Display Enabler 2.0 to get Display Manager 2.0 features. Keywords: Display Manager, FKey, resolution, DMFkey

[Next](DMFkey.c.md)

