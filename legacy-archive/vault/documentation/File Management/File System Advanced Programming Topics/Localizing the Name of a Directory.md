---
title: File System Advanced Programming Topics
apple_id: TP40010765
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemAdvancedPT/LocalizingtheNameofaDirectory/LocalizingtheNameofaDirectory.html
archived_at: '2026-07-15T07:31:56.767725Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Advanced Programming Topics](About%20Advanced%20File%20System%20Topics.md)



# Localizing the Name of a Directory

If your application installs any custom support directories, you can provide [localized](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Internationalization.html#//apple_ref/doc/uid/TP40008195-CH23) versions for your directory names. Providing localized names is not required and should be done only for directories whose names you know in advance. It should not be done for any user-specified directories. When the appropriate preferred language is selected, the Finder displays the localized directory names you provide.

To provide a localized display name for a directory, do the following:

1. Add the extension `.localized` to the directory name.
2. Create a subdirectory inside the directory called `.localized`. (You must create this directory programmatically or using the Terminal application.)
3. Inside the `.localized` subdirectory, create a strings files for each localization you support.

Each strings file is a Unicode text file that contains the appropriately localized name of the directory. The name of each strings file should be an appropriate two-letter language code followed by the `.strings` extension. For example, a localized Release Notes directory with English, Japanese, and German localizations would have the following directory structure:

```
Release Notes.localized/
    .localized/
        en.strings
        de.strings
        ja.strings
```

Inside each strings file, include a single string entry to map the nonlocalized directory name to the localized name. When specifying the original directory name, do not include the `.localized` extension you just added. For example, to map the name “Release Notes” to a localized directory name, each strings file would have an entry similar to the following:

```
"Release Notes" = "Localized name";
```

For information on creating a strings file, see _[Internationalization and Localization Guide](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_.

