---
title: Documentation Set Guide
apple_id: TP40005266
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2009-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/Documentation_Sets/800-Documentation-Set_Property_List_Key_Reference/docset_plist_ref.html
archived_at: '2026-07-15T07:24:25.725852Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Documentation Set Guide](Introduction.md)


[Next](Documentation-Set%20Nodes%20Schema%20Reference.md)[Previous](docsetutil%20Reference.md)

# Documentation-Set Property List Key Reference

This chapter describes the property list keys that you can use in the `Info.plist` file for your documentation set bundle. It lists only those keys that have particular relevance to documentation sets. For a list of the core OS X property list keys, see “Property List Key Reference.”

The default region for the bundle. This is typically the language in which the documentation set is developed. Xcode uses the language specified by this key as the default language if a documentation set resource cannot be found for the user’s preferred region or language.

This is a standard OS X property list key. See Property List Key Reference for more information.

A reverse-domain name style string that uniquely identifies the documentation set bundle, such as `com.apple.ADC_Reference_Library.CoreReference`. This string should be globally unique. This string should not change between different versions of the same documentation set.

Xcode uses the identifier string to match an installed documentation set with a specific entry in the RSS/Atom feed specified by the feed URL.

This is a standard OS X property list key. See Property List Key Reference for more information.

The name of the documentation set. Xcode uses this name to identify the documentation set to the user. It appears in Xcode Documentation preferences. This string can be localized.

This is a standard OS X property list key. See Property List Key Reference for more information.

The version number of the documentation set bundle. This value is compared to the version number for the documentation set with the same identifier in the web feed to determine whether a new version is available for download.

This is a standard OS X property list key. See Property List Key Reference for more information.

An optional URL pointing to a parallel location on the web where the contents of the documentation set’s Documents folder can be found. When browsing or searching the installed documentation set, if Xcode cannot find a file in the local installation, it tries to load the file from the web site specified by this key.

For example, if Xcode is trying to access a file at the path—relative to the documentation set’s `Documents` directory—`PlugIns/MyPlugIn.html` and cannot find that file, it checks to see if the documentation set specifies an alternate fallback URL. If that fallback URL exists—say, for example `http://mycompany.com/Documentation/MyNiftyDocSet`—Xcode looks for the missing file at `http://mycompany.com/Documentation/MyNiftyDocSet/PlugIns/MyPlugIn.html`.

If you have a large documentation set, you can use a fallback website to reduce its footprint. You can install only the essential parts of your documentation in the local copy of the documentation set bundle, while less commonly used documents may exist only on your website.

A short name describing the overall group of documentation to which this documentation set belongs. This name normally does not appear to the Xcode user, although Xcode uses this name as the publisher name if you do not set an explicit publisher name.

This display name is typically a name identifying the provider of the documentation set, such as "Apple." This string can be localized.

The URL of an RSS/Atom feed that Xcode can use to learn about updates or additional documentation sets available from the same publisher. A single publisher can provide multiple RSS/Atom feeds, with each feed providing information about multiple, related documentation sets. Any given documentation set should be listed in only one of these feeds.

A string specifying the unique identifier for the publisher.

For example: `com.mycompany.myproduct.documentation`

All documentation sets that have the same publisher identifier are grouped under the same publisher name, even if the documentation sets are provided by different feeds. If missing, Xcode uses the `DocSetFeedURL` as the identifier, in which case the feed is treated as its own publisher.

A string specifying the display name for the publisher.

For example: `My Company`

If missing, Xcode uses the `DocSetFeedName`. You can localize this string.

A string specifying the distinguished name of the signer of the documentation set certificate.

For example: `C=US,O=Apple Computer\, Inc.,OU=mac.com,CN=myMacAcct`.

A string specifying the distinguished name of the issuer of the documentation set certificate.

For example: `C=US,O=Apple Computer\, Inc.,OU=Apple Computer Certificate Authority,CN=Apple .Mac Certificate Authority`.

A copyright string. This string is displayed in the Info window for the documentation set.

This is a standard OS X property list key. See Property List Key Reference for more information.

[Next](Documentation-Set%20Nodes%20Schema%20Reference.md)[Previous](docsetutil%20Reference.md)

