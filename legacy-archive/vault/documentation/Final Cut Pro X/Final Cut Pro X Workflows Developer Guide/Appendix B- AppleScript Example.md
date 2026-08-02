---
title: Final Cut Pro X Workflows Developer Guide
apple_id: TP40013781
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/FinalCutProX/Conceptual/FinalCutProXWorkflowsGuide/AppleScriptExample/AppleScriptExample.html
archived_at: '2026-07-15T07:32:28.009714Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Final Cut Pro X Workflows Developer Guide](About%20Final%20Cut%20Pro%20X%20Workflows.md)


[Next](Appendix%20C-%20Share%20Metadata.md)[Previous](Appendix%20A-%20ProVideo%20Asset%20Management%20Suite.md)

# Appendix B: AppleScript Example

This appendix presents a simple AppleScript fragment and the resulting event trace that illustrates the interaction between Final Cut Pro X and another application through Apple events. You can use this script fragment to test your application’s ability to interact with Final Cut Pro X.

__Listing 5-1__  AppleScript fragment

```
tell application "SimpleAssetManager"
    make new asset with properties ¬
        {name:"MyNewAsset", metadata:{|com.apple.proapps.share.episodeID|:"MyNewEpisode"}, data options:{|availableMetadataSets|:{"Camera View", "General View"}}} ¬

    set newAsset to result
    set theLocation to location info of newAsset
    set theLibraryLocation to library info of newAsset
    set theMetadata to metadata of newAsset
    set theDataOptions to data options of newAsset
end tell
```

The following Apple event trace outlines events and replies when the AppleScript fragment above runs:

__Listing 5-2__  Apple event trace

```swift
tell application "SimpleAssetManager"
    make new asset with properties {name:"MyNewAsset", metadata:{|com.apple.proapps.share.episodeid|:"MyNewEpisode"}, data options:{availableMetadataSets:{"Camera View", "General View"}}}
        --> asset id "SSO-29842-2" of document "Untitled"
    get location info of asset id "SSO-29842-2" of document "Untitled"
        --> {has media:true, has description:true, base name:"MyNewAsset", folder:file "Lucca:Users:jane:Movies:"}
    get library info of asset id "SSO-29842-2" of document "Untitled"
        --> {has library description:true, has archive:true, library folder:file "Lucca:Users:jane:Movies:", library base name:"MyNewAssetLibrary"}
    get metadata of asset id "SSO-29842-2" of document "Untitled"
        --> {|com.apple.simpleassetmanager.preparedasset|:"1", |com.apple.simpleassetmanager.managedasset|:"1", |com.apple.quicktime.description|:"", |com.apple.simpleassetmanager.expeirationdate|:"2016-09-30 00:57:09 +0000", |com.apple.proapps.share.episodeid|:"MyNewEpisode", |com.apple.proapps.share.id|:"", |com.apple.proapps.share.episodenumber|:"0"}
    get data options of asset id "SSO-29842-2" of document "Untitled"
        --> {metadataSet:"None", descriptionVersion:"Previous Version"}
end tell

Result:
{metadataSet:"None", descriptionVersion:"Previous Version"}
```

[Next](Appendix%20C-%20Share%20Metadata.md)[Previous](Appendix%20A-%20ProVideo%20Asset%20Management%20Suite.md)

