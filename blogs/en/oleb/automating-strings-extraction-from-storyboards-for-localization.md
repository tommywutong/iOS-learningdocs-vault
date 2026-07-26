---
title: Automating Strings Extraction From Storyboards for Localization
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/02/automating-strings-extraction-from-storyboards-for-localization/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:e120d702cf8322e3'
translated: false
---

> 原文：[Automating Strings Extraction From Storyboards for Localization](https://oleb.net/blog/2013/02/automating-strings-extraction-from-storyboards-for-localization/)　·　Ole Begemann

# Automating Strings Extraction From Storyboards for Localization

**Update April 24, 2014:** I just learned that Apple does in fact provide a coomand line tool named AppleGlot that supports incremental localization of .strings files, NIBs, and storyboards. AppleGlot just got updated to version 4.0 (v159.1) on April 15, 2014, and the release notes list support for Xcode 5 file formats. I haven’t tried it myself but if you are looking for a tool to help you with incremental localization, I suggest you check it out. Registered Apple developers can download AppleGlot from [the downloads section in Apple’s dev center](https://developer.apple.com/downloads/).

With OS X 10.8 and iOS 6.0 Apple introduced the concept of a _base internationalization_ to Xcode. While the old way of localizing a Cocoa app involved maintaining multiple copies of your NIB or storyboard files (one for each language), an app using base internationalization has just one set of storyboards or NIBs, localized to the app’s default language.

# Base Localization

The localized content for your user interfaces is maintained in `.strings` files (one per language and NIB or storyboard file). At runtime, the NIB loading system automatically replaces the user-facing strings in the NIB with the appropriate localized variant from the corresponding strings file.

Base internationalization is the perfect companion to [Cocoa autolayout](https://developer.apple.com/library/mac/#documentation/UserExperience/Conceptual/AutolayoutPG/Articles/Introduction.html), another recent addition to AppKit and UIKit. In the past, it was often necessary to maintain multiple copies of a NIB not just for translation, but because localizations required different UI layouts due to vast discrepancies in text lengths between languages. With autolayout, a single base layout can respond much better to varying text lengths.

# Setting Up Base Localization In Xcode

To set up base localization in Xcode, go to your project settings and on the Info pane, select “Use Base Internationalization” checkbox. Xcode will display a popup, asking you which of the languages your app already supports should serve as the basis for the new base localization. When you approve the selection, Xcode treats the storyboards or NIBs for the language you selected as the Base localization. The files are moved into the new `Base.lproj` directory.

![Selecting Base Internationalization in Xcode 4](https://oleb.net/media/xcode-selecting-base-internationalization.png)

![Selecting the source language to use for creating the base localization in Xcode](https://oleb.net/media/xcode-popup-creating-base-localization.png)

<sub>Setting up base internationalization in Xcode.</sub>

If you already have translated NIBs or storyboards in other languages, Xcode does not convert them to using the base localization automatically. The idea behind this is that you are free to use a mixed approach: use base internationalization for most languages you support, but make a full copy of your storyboard for one specific language (for example, because its layout requirements are beyond what can be done with autolayout).

In most cases, you will want to convert your existing translated NIBs to the new model. To do that, open the file in Xcode and open the File Inspector. In the Localization section, you can choose between “Interface Builder” (the old way) and “Localizable Strings” (base internationalization) for each language. Selecting “Localizable Strings” will extract the current user-facing strings from the NIB file and place them into a strings file, then delete the now-unnecessary NIB or storyboard file from disk.

![Converting a storyboard file to base localization in Xcode](https://oleb.net/media/xcode-file-inspector-localization-settings.png)

![Confirmation alert in Xcode when converting a storyboard file to base localization](https://oleb.net/media/xcode-convert-existing-localization-to-base.png)

<sub>Converting an already translated storyboard file to base internationalization.</sub>

Should you later add a new localization to your project, Xcode offers you the same choice between “Localizable Strings” and “Interface Builder”, this time extracting the strings to be localized from the base NIB file or storyboard.

**Update March 22, 2013:** If you are using NIB files, you may find that your app no longer works after enabling the base localization. Instead, error messages that indicate that the app could not load one or more NIB files appear in the console:

```
[PreferencesWindowController loadWindow]: failed to load window nib file 'Preferences'.
```

This is due to a bug in Xcode that causes Xcode to not compile localized `.xib` into `.nib` files during the build process. At runtime, the NIB loader looks for NIB files and ignores the XIB files in the app bundle. The [simple fix](http://stackoverflow.com/a/5692278/116862): select the XIB file(s) in Xcode, change the file type to something else, and then change it back to the Default type. After doing this, clean and rebuild.

As documented by the Stack Overflow thread, the bug was present in April 2011 (Xcode 4.0), and I confirmed it is still there in Xcode 4.6.1.

# Automating Strings Extraction

Unfortunately, the automatic conversion from Interface Builder to strings file is a one-time process. Xcode does not automatically update the strings files whenever you make changes to your base NIB files or storyboards. And manual updating is not only tedious but made especially hard because of the obscure keys Xcode uses to identify an object. For example, the label for a button may appear under the key `"hzx-cM-fkt.normalTitle"` in the strings file. While the button’s object ID `hzx-cM-fkt` can be found in Interface Builder’s Identity Inspector, dealing with those IDs manually is not much fun.

Fortunately, there is a better way. MacRumors forum user [mikezang has written a handy script](http://forums.macrumors.com/showpost.php?p=16060008&postcount=4) that uses Apple’s [ibtool](http://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man1/ibtool.1.html) to extract all translatable strings from the base storyboard and then merges the new translatable strings with your existing translations in the per-language strings files. It’s almost[1](#fn:1) perfect.

mikezang’s original script relies on the premise that, for each storyboard file in the `Base.lproj` folder, a corresponding `.strings` file exists in the same folder. The script compares the modification dates of these files to determine if the storyboard has been modified. Normally, you would have to create this base file manually. I updated the script slightly to automatically create the base `.strings` file if it doesn’t exist. Here is my modified version:

```
#!/bin/sh
#
# update_storyboard_strings.sh - automatically extract translatable strings from storyboards and update strings files
# Based on http://forums.macrumors.com/showpost.php?p=16060008&postcount=4 by mikezang

storyboardExt=".storyboard"
stringsExt=".strings"
newStringsExt=".strings.new"
oldStringsExt=".strings.old"
localeDirExt=".lproj"

oldIFS=$IFS
IFS=$'\n'

# Find storyboard file full path inside project folder
for storyboardPath in `find . -name "*$storyboardExt" -print`
do
    # Get Base strings file full path
    baseStringsPath=$(echo "$storyboardPath" | sed "s/$storyboardExt/$stringsExt/")

    # Create base strings file if it doesn't exist
    if ! [ -f $baseStringsPath ]; then
      touch -r $storyboardPath $baseStringsPath
      # Make base strings file older than the storyboard file
      touch -A -01 $baseStringsPath
    fi

    # Create strings file only when storyboard file newer
    if find $storyboardPath -prune -newer $baseStringsPath -print | grep -q .; then
        # Get storyboard file name and folder
        storyboardFile=$(basename "$storyboardPath")
        storyboardDir=$(dirname "$storyboardPath")

        # Get New Base strings file full path and strings file name
        newBaseStringsPath=$(echo "$storyboardPath" | sed "s/$storyboardExt/$newStringsExt/")
        stringsFile=$(basename "$baseStringsPath")

        ibtool --export-strings-file $newBaseStringsPath $storyboardPath

        # ibtool sometimes fails for unknown reasons with "Interface Builder could not open
        # the document XXX because it does not exist."
        # (maybe because Xcode is writing to the file at the same time?)
        # In that case, abort the script.
        if [[ $? -ne 0 ]] ; then
            echo "Exiting due to ibtool error. Please run `killall -9 ibtoold` and try again."
            exit 1
        fi

        # Only run iconv if $newBaseStringsPath exists to avoid overwriting existing
        if [ -f $newBaseStringsPath ]; then
          iconv -f UTF-16 -t UTF-8 $newBaseStringsPath > $baseStringsPath
          rm $newBaseStringsPath
        fi

        # Get all locale strings folder
        for localeStringsDir in `find $storyboardPath -name "*$localeDirExt" -print`
        do
            # Skip Base strings folder
            if [ $localeStringsDir != $storyboardDir ]; then
                localeStringsPath=$localeStringsDir/$stringsFile

                # Just copy base strings file on first time
                if [ ! -e $localeStringsPath ]; then
                    cp $baseStringsPath $localeStringsPath
                else
                    oldLocaleStringsPath=$(echo "$localeStringsPath" | sed "s/$stringsExt/$oldStringsExt/")
                    cp $localeStringsPath $oldLocaleStringsPath

                    # Merge baseStringsPath to localeStringsPath
                    awk 'NR == FNR && /^\/\*/ {x=$0; getline; a[x]=$0; next} /^\/\*/ {x=$0; print; getline; $0=a[x]?a[x]:$0; printf $0"\n\n"}' $oldLocaleStringsPath $baseStringsPath > $localeStringsPath

                    rm $oldLocaleStringsPath
                fi
            fi
        done
    else
        echo "$storyboardPath file not modified."
    fi
done

IFS=$oldIFS
```

[Download the script from GitHub](https://github.com/ole/Storyboard-Strings-Extraction).

If you automate running the script during the Xcode build process, your strings files will get updated automatically upon the next build whenever a storyboard has changed. To do that, navigate to the Build Phases tab in your target settings in Xcode. Click the “Add Build Phase” button and choose “Add Run Script”. Paste the script code into the text area that appears. Alternatively, download the script and save it to a `scripts` folder in your project directory. Don’t forget to make it executable:

```
> chmod +x update_storyboard_strings.sh
```

Now, add a Run Script build phase as described above and enter the path of the script file into the text area:

```
${PROJECT_DIR}/scripts/update_storyboard_strings.sh
```

That’s it!

![Adding a Run Script build phase in Xcode](https://oleb.net/media/xcode-build-phase-run-script.png)

<sub>The Run Script build phase in Xcode's target settings.</sub>

**Update April 30, 2013:** A reader reported problems with the script. In his testing, some strings files containing Chinese characters were cut off somewhere in the middle when run through the final step of the script where the existing translations are merged with the newly added strings. It is hard to reproduce for me but it seems the script has problems with certain multi-byte characters (which I admit is a ridiculous bug for a localization tool).

The merge step uses `awk` and, according to my limited reserach, it seems the version of `awk` that comes with OS X (BSD awk) does indeed have some issues with non-Latin characters. Another version, GNU awk or simply `gawk` handles UTF-8 better. So if you encounter this problem, please try installing GNU awk on your machine with Homebrew:

```
> brew install gawk
```

Then replace the `awk` command in the script with `gawk`:

```
...
# Merge baseStringsPath to localeStringsPath
gawk 'NR == FNR && /^\/\*/ {x=$0; getline; a[x]=$0; next} /^\/\*/ {x=$0; print; getline; $0=a[x]?a[x]:$0; printf $0"\n\n"}' $oldLocaleStringsPath $baseStringsPath > $localeStringsPath
...
```

Please let me know if this solution works for you.

**Update February 26, 2014:** With Xcode 5.0.2, the `ibtool` command used by the script sometimes fails with a weird error message:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>com.apple.ibtool.errors</key>
    <array>
        <dict>
            <key>description</key>
            <string>Interface Builder could not open the document "Main.storyboard" because it does not exist.</string>
        </dict>
    </array>
</dict>
</plist>
```

I have not been able to figure out the cause of this error; the storyboard file definitely exists. (Maybe Xcode is accessing the storyboard file at the same time?). What’s worse is that the script did not handle this error until now and continued to run as if the `ibtool` command had succeeded. It would overwrite existing strings files with empty data and potentially cause the loss of existing localizations.

I have updated the script in this post and [on GitHub](https://github.com/ole/Storyboard-Strings-Extraction) with a fix. The call to `ibtool` can still fail, but the script will now stop immediately if that happens and ask you to run it again. If the error occurs repeatedly, the only “fix” I have found is to run this command in Terminal:

```
> killall -9 ibtoold
```

It’s not a perfect solution, but it seems to work okay in my limited testing. If you know more about the `ibtool` error I mentioned or what `ibtoold` may have to do with it, I’d love to hear from you.

**Update August 25, 2014:** I created [a regular GitHub repository](https://github.com/ole/Storyboard-Strings-Extraction) for the script in place of the original Gist. Pull requests welcome!

1. In its current form, the script only works with storyboards but it should be easy to adapt to NIB files. Simply replace the file extension `".storyboard"` with `".xib"` at the top of the file. [↩︎](#fnref:1)
