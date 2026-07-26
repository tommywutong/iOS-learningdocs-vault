---
title: macOS Accessibility Keyboard
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/accessibility-keyboard/'
original_language: en
published: 2019-08-12
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:f4c3a81c7c2bc5c4'
translated: false
---

> 原文：[macOS Accessibility Keyboard](https://nshipster.com/accessibility-keyboard/)　·　NSHipster (Mattt)

# [macOS Accessibility Keyboard](https://nshipster.com/accessibility-keyboard/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  August 12^th, 2019

For a while now, the distinction between “desktop” and “mobile” has become increasingly tenuous. As the computers in our pockets grow ever more capable, they more closely resemble the computers typically situated on our desks and laps. This trend was especially pronounced in this year’s WWDC, with the announcement of [Catalyst](https://developer.apple.com/ipad-apps-for-mac/) and [iPadOS](https://www.apple.com/ipados/).

Today, what’s the difference between a MacBook and an iPad? Practically speaking, you might point to the presence or absence of a physical keyboard, a SIM card, or an ARM processor _(and if the rumors about next year’s MacBook models are to believed, those latter two may soon cease to be a distinction)._

For many of us, a physical keyboard is the defining trait that _makes_ a computer a “desktop” computer in the traditional sense; when you purchase an external keyboard for your iPad, you do so to make it “desktop”-like. But for many others — including those of us with a physical disability — a typewriter-like keyboard is but one of many input methods available to desktop users.

This week on NSHipster, we’re taking a look at the macOS Accessibility Keyboard. Beyond its immediate usefulness as an assistive technology, the Accessibility Keyboard challenges us to think differently about the nature of input methods and any remaining distinction between mobile and desktop computers.

---

Introduced in macOS High Sierra, the [Accessibility Keyboard](https://support.apple.com/accessibility/mac) lets you type and interact with your Mac without the use of a physical keyboard.

To turn it on, open System Preferences, click the Accessibility preference pane, select “Keyboard” under the “Interactions” section in the sidebar. (Alternatively, you can search for “Accessibility Keyboard” and navigate to the first result).

![Accessibility Keyboard Panel Editor](https://nshipster.com/assets/facetime-picture-in-picture-23cb401da9ed13fb26dd57fbb0d5b74c2a0d458bd65101bff06e881adcdc8a3992405c6fc69fdb0612c699266ec6301b0b44f930113ff2c6f2676ac57b5bda46.png)

Click the checkbox labeled “Enable Accessibility Keyboard” to present the accessibility keyboard over the windows of the frontmost app.

![](https://nshipster.com/assets/accessibility-keyboard-keyboard-b733dcacf73b21973f2383136557fae33050bf68b2e44cb540bd942d23cff5b0274edbb9b01b6b29839c365c69d2006a4147af4ec9f8ade23867672db89a864f.png)

The software keyboard reproduces the layout of your hardware keyboard. The modifier keys outlined in red (⌘, ⇧, ⌥) are “sticky keys” and remain active until a non-“sticky” key is activated, allowing for capital letters and keyboard shortcuts. Along the top row are iOS-style suggestions that update automatically as you type.

However, the most interesting feature of the Accessibility Keyboard is tucked behind the ⚙︎ button on the top right corner — _the ability to customize and create your own keyboards!_

![](https://nshipster.com/assets/accessibility-keyboard-menu-customize-b3155e66f69712b75cb671d9e6d32c1d9278ae9645c5a61b509ea2351a04dc2907b4216a08fb8f7a89194afcc5cd2deaf82dd284bfe69648d571ec3e4bd47545.png)

## Customizing and Creating Your Own Accessibility Keyboards

Panel Editor is a built-in app that lets you edit Accessibility Keyboard panels.

![Accessibility Keyboard Panel Editor window and icon](https://nshipster.com/assets/accessibility-keyboard-panel-editor-d16bd04ac901e6202bae36a580210b1fa6316619c16719274630ca7bbb28ed0d5de477c4a871d6b887a2f57282872f50ab357c1a8b828f4b577e64e5643e671d.png)

For something so obscure, the Panel Editor app is remarkably well made. Adding, moving, and editing buttons on a panel is a cinch. You can even click and drag to select and move multiple buttons at once, and group buttons together at your convenience.

Each button has a name as well as options for font size, color, and position. By default, the name appears in the button itself, but you can specify an image to display instead.

You can configure a button to perform any one of the following actions when clicked:

- None
- Go Back _(navigate between panels in Accessibility Keyboard)_
- Open Panel
- Show / Hide Toolbar
- Dwell _(relevant to head- or eye-tracking technology, and other hardware switches)_
- AppleScript
- Enter Text
- Press Keys
- Open App
- System Event
- Typing Suggestions

Of these, “Enter Text” is the most common. We’ll use that in our next example as a way to solve the problem of creating input methods for scripts without a keyboard.

### Creating an IPA Keyboard

Standard Latin script is insufficient for expressing phonetics, how a word sounds when spoken. As English speakers, we know this all too well. That’s why linguists invented their own script, the International Phonetic Alphabet (IPA). Whereas typical letters may have different pronunciations across dialects (/tə.ˈme͡ɪ.do͡ʊ/, /tə.ˈmɑ.to͡ʊ/) — or even within the same word (like the letter “a” in “application”) — IPA symbols represent a single sound, or phoneme; the mid-central vowel, “ə” (a.k.a “schwa”) sounds the same whether its part of an English word or a Japanese word or nonsensical babbling.

Working with IPA on computers has pretty much always been a PITA, for three reasons:

**Incomplete Text Encoding** Until Unicode version 6.1, some IPA symbols didn’t have a specified code point, forcing linguists to either use a similar-looking character or define _ad hoc_ encodings within a [Private Use Area](https://en.wikipedia.org/wiki/Private_Use_Areas). **Limited Font Support** It’s one thing to have a specified code point. Having a font that can shape, or render that code point correctly is another matter entirely. **Lack of Input Methods** Just because the computer can represent and render a character doesn’t mean that you, as a user, can produce that character in the first place. Typing on a QWERTY keyboard, we take for granted being able to type the j key to produce the letter “j”. But what if you wanted to type “[ʝ](https://en.wikipedia.org/wiki/Voiced_palatal_fricative)”?   
   
 For all too many people, the answer is _“Google and copy-paste”_.

Fortunately, the first and second of these three challenges are no longer an issue on modern operating systems: Unicode provides code points for all of the [IPA characters](https://en.wikipedia.org/wiki/Phonetic_symbols_in_Unicode), and most platforms natively render them all without having to install a custom font. However, the problem of input methods remains an open question.

SIL International hosts [an IPA keyboard layout](http://scripts.sil.org/cms/scripts/page.php?item_id=UniIPAKeyboard#79dbd88a) by Joan Wardell. There’s also the [SuperIPA](https://www.kreativekorp.com/software/keyboards/superipa/) keyboard — based on CXS, a variant of [X-SAMPA](https://en.wikipedia.org/wiki/X-SAMPA) — by Kreative Korporation. You could also use [IPA Palette](https://github.com/K8TIY/IPAPalette) by Brian “Moses” Hall.

But if none of these tick all of your boxes in terms of usability of ergonomics, the Accessibility Keyboard Panel Editor provides an easy way for anyone to hand-roll a bespoke solution:

![](https://nshipster.com/assets/accessibility-keyboard-custom-keyboard-ipa-chart-72d6a81e3b58515d75828a48fadeb44e6d590062aff527ced91425b1af628b09d7e1113c75309826f7161e7321befe90594431674ac9c098db1c0474b7c89a87.png)

This keyboard layout was created with Panel Editor and is modeled after the [official IPA Chart](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet_chart), with symbols arranged by place and manner of articulation. It’s not nearly as efficient as any of the aforementioned keyboard layouts (nor is it as complete), but anyone familiar with IPA can use it for transcription immediately without additional training.

---

If you’re a developer, there’s a good chance that your next questions are _“What does this file format look like?”_ and _“Can I generate these with code rather than a GUI?”_.

The short answers are “A Bundle of Property Lists”, and “Yes!”. Read on for the full breakdown:

---

## Inspecting the Accessibility Keyboard File Format

The keyboard panel bundles themselves can be tricky to find if you don’t know what you’re looking for. On macOS Mojave, any custom panels you make can be found within the `~/Library/Application Support/com.apple.AssistiveControl/` directory in bundles with a `.ascconfig` file extension.

The bundle comprises a top-level Info.plist file and a Resources directory containing an index of assets (along with any asset files, like button images) as well as a file named `PanelDefinitions.plist`.

```
$ tree ~/Library/Application Support/com.apple.AssistiveControl/dwellControlUserPanels1.ascconfig/
Contents
├── Info.plist
└── Resources
    ├── AssetIndex.plist
    └── PanelDefinitions.plist
```

Opening up `PanelDefinitions.plist` reveals the inner structure of our custom virtual keyboard layout:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Panels</key>
	<dict>
		<key>USER.80B26730-BB8A-41A5-8E70-79AA134F9D0E</key>
		<dict>
			<key>AssociatedApplications</key>
			<array>
				<dict>
					<key>ApplicationBundleID</key>
					<string>com.apple.Notes</string>
					<key>ApplicationDisplayName</key>
					<string>Notes</string>
					<key>ApplicationPath</key>
					<string>/Applications/Notes.app</string>
				</dict>
			</array>
			<key>DisplayOrder</key>
			<integer>1</integer>
			<key>GlidingLensSize</key>
			<integer>5</integer>
			<key>HasTransientPosition</key>
			<false/>
			<key>HideHome</key>
			<false/>
			<key>HideMinimize</key>
			<false/>
			<key>HidePanelAdjustments</key>
			<false/>
			<key>HideSwitchDock</key>
			<false/>
			<key>HideSwitchDockContextualButtons</key>
			<false/>
			<key>HideTitlebar</key>
			<false/>
			<key>ID</key>
			<string>USER.80B26730-BB8A-41A5-8E70-79AA134F9D0E</string>
			<key>Name</key>
			<string>Keyboard - IPA</string>
			<key>PanelObjects</key>
			<array>
                …
            </array>
        </dict>
    </dict>
</dict>
```

The `PanelObjects` key is associated with an array of dictionaries, each representing a single button. Fortunately, he majority of the key names are self-explanatory:

```
<dict>
	<key>ButtonType</key>
	<integer>0</integer>
	<key>DisplayColor</key>
	<string>0.145 0.145 0.145 1.000</string>
	<key>DisplayImageResourceIsTemplate</key>
	<false/>
	<key>DisplayText</key>
	<string>p</string>
	<key>DisplayTextLocation</key>
	<string>DisplayInside</string>
	<key>DisplayTextPosition</key>
	<string>Center</string>
	<key>DisplayTheme</key>
	<string>DisplayThemeDefault</string>
	<key>FontSize</key>
	<real>20</real>
	<key>ID</key>
	<string>Button.7B824E7E-9AB8-42E3-BA7B-B56924B45554</string>
	<key>PanelObjectType</key>
	<string>Button</string>
	<key>Rect</key>
	<string>{{0, 5}, {35, 35}}</string>
	<key>Actions</key>
	<array>
		<dict>
			<key>ActionParam</key>
			<dict>
				<key>CharString</key>
				<string>p</string>
				<key>isStickyKey</key>
				<false/>
			</dict>
			<key>ActionRecordedOffset</key>
			<real>0.0</real>
			<key>ActionType</key>
			<string>ActionPressKeyCharSequence</string>
			<key>ID</key>
			<string>Action.0AE7D5DD-C588-40FA-942E-89E25FD81EEA</string>
		</dict>
	</array>
</dict>
```

The takeaway from looking at the file format is that it’d be very easy to generate Accessibility Keyboard panels in code, rather than using the Panel Editor app. (In fact, we used find-and-replace to bulk resize the buttons in the IPA keyboard, a task that would have otherwise taken 100⨉ longer).

## Additional Use Cases

There are dozens of scripts comprising hundreds of characters that lack a dedicated keyboard layout. And the macOS Accessibility Keyboard offers a wonderful, built-in solution for producing these characters.

But what else could you do with this technology, now that you know it exists?

Here are a few ideas for you to consider:

### Templating Frequent Communications

Do you find yourself writing the same things over and over again in emails or GitHub Issues? Create a custom, virtual keyboard to summon [boilerplate](https://nshipster.com/swift-gyb/) with the click of your mouse or the tap of your trackpad.

### Generative Text

The Accessibility Keyboard isn’t limited to canned responses. Thanks to its AppleScript integration, you can populate text dynamically from virtually any source.

For example, you could create a Fortune button that inserts a (pseudo)random entry from the [`fortune`](https://en.wikipedia.org/wiki/Fortune_%28Unix%29) program, with the following AppleScript:

```
set fortune to do shell script "/usr/local/bin/fortune"
set the clipboard to fortune as text
delay 0.01
tell application "System Events" to tell (name of application processes whose frontmost is true) to keystroke "v" using command down
```

Obligatory `fortune` output:

> If your bread is stale, make toast.

### Sound Board

Do you aspire to be a ~~drive-time radio DJ~~ live streamer? Use the Accessibility Keyboard to trigger funny sound effects at will to delight your throng of fans.

![](https://nshipster.com/assets/accessibility-keyboard-panel-editor-sounds-3f272093e4d72c3d040941c70b16913a6faf5de622bb2d237ecc153ed2b0b8b0171af5dedcd5fc83d09e2169056bea2e5d20d2ece0500361da609317856ec41a.png)

```
do shell script "afplay /System/Sounds/Sosumi.aiff"
```

### World Domination

AppleScript gives you the closest thing to complete, programmatic access to the entire system.

Set a button to kick off a build of your app, or send a message on Slack, or turn on the lights in your house, or play your theme song!

---

The Accessibility Keyboard serves as a powerful, built-in, and omnipresent interface to whatever functionality you desire — without going through all the trouble of building an app.

Because, if you think about it, is there any real difference between the j key on your keyboard and a hypothetical Party button on a virtual keyboard?

The strong connection between the word “computer” and typewriter keyboards is merely a historical one. The rise of smartphones and smartwatches help illustrate this. Any distinction between the computers in your hand, on your wrist, or on your desk is ultimately insignificant. All computers are the same; they’re all force multipliers.

Once you separate “desktop” computers from the shape of their primary interface, you can start to fully appreciate the full capabilities of what’s at our fingertips.
