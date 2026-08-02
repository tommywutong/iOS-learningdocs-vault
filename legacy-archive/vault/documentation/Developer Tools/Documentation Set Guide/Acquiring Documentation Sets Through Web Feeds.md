---
title: Documentation Set Guide
apple_id: TP40005266
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2009-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/Documentation_Sets/070-Acquiring_Documentation_Sets_Through_Web_Feeds/acquiring_docsets.html
archived_at: '2026-07-15T07:24:25.698777Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Documentation Set Guide](Introduction.md)


[Next](Testing%20and%20Packaging%20Documentation%20Sets.md)[Previous](Internationalizing%20Documentation%20Sets.md)

# Acquiring Documentation Sets Through Web Feeds

Xcode supports automatic detection and download of documentation set updates. You can take advantage of this feature by providing an RSS or Atom feed (also known as _web feeds_) to publish content updates for your own documentation sets. Users can subscribe to your web feed from Xcode Documentation preferences. They can check for and download updates to installed documentation sets, or download new documentation sets.

Xcode uses the Publication Subscription framework to subscribe to documentation set feeds. It can recognize and support the same web feed formats supported by that framework. Currently, this includes RSS 1.0, RSS 2.0, and Atom. This chapter uses Atom in all of its explanations and examples. To learn more about the elements in an Atom feed, visit [http://atomenabled.org/developers/syndication](http://atomenabled.org/developers/syndication).

This chapter describes the key elements used to describe an Atom feed and a documentation set entry. It also includes an example Atom feed.

A feed consists of metadata, which provides general information about the feed and its contents, and a series of entries. Each entry represents a _documentation set update_.

The feed is represented by the standard Atom element, `Feed`. To describe a feed you must specify the following information:

- The publisher of the feed (`publisherName` and `publisherID`)
- The unique identifier of the feed (`id`)
- The title of the feed (`title`)
- The last time the feed was modified (`updated`)

As of Xcode 3.2, you have the option to use these elements on the entire feed:

- `minimumXcodeVersion`: Specifies the earliest Xcode release that is to download the feed.
- `maximumXcodeVersion`: Specifies the latest Xcode release that is to download the feed.

Listing 7-1 shows how you might use these elements to describe a feed. The Atom specification also defines other elements that let you specify additional information such as the author, copyright information and so forth.

__Listing 7-1__  Describing a feed

```
<feed xmlns="http://www.w3.org/2005/Atom"
  xmlns:docset="http://developer.apple.com/rss/docset_extensions"
  xml:lang="en">
  <docset:publisherName>Apple</docset:publisherName>
  <docset:publisherID>com.apple.adc.documentation</docset:publisherID>
  <id>http://developer.apple.com/</id>
  <title type="text">Apple Developer Documentation</title>
  <updated>2006-03-24T12:00:00Z</updated>
  ...
</feed>
```


As you learned in the previous section, each entry in the web feed corresponds to a single documentation set download. You can publish updates to multiple documentation sets with a single web feed.

You specify an entry using the standard Atom element, Entry. For each entry, or documentation set, you must specify:

- The unique identifier for the entry (`id`). This can be any unique uniform resource name (URN).
- The name of the documentation set (`title`). This must match the value of the documentation set’s `CFBundleName` property.
- The last time the entry was modified (`updated`).
- A link to the documentation set download (`link`).
- The documentation set identifier (`docset:identifier`). This must match the value of the documentation set’s `CFBundleIdentifier` property.
- The documentation set version (`docset:version`). This must match the value of the documentation set’s `CFBundleVersion` property.

The first four elements are standard Atom elements, described further at [http://atomenabled.org/developers/syndication](http://atomenabled.org/developers/syndication). You can also include other elements defined by the Atom specification.

The `identifier` and `version` elements are custom elements defined by the `docset` namespace. The `docset` namespace also defines several optional elements:

- `minimumXcodeVersion`: Specifies the earliest Xcode release that is to download the documentation set.
- `maximumXcodeVersion`: Specifies the latest Xcode release that is to download the documentation set.
- `signer`: Specifies the distinguished name of the signer of the documentation set certificate.
- `issuer`: Specifies the distinguished name of the issuer of the documentation set certificate.

Listing 7-2 shows how you can use the elements described in this section to create a web feed entry for a documentation set.

__Listing 7-2__  Describing a documentation set entry

```
<entry>
  <id>tag:apple.com/CoreRef/2004</id>
  <title type="text">Core Reference Library</title>
  <summary type="text">Includes reference for Carbon, Cocoa, and other frameworks.</summary>
  <updated>2006-03-24T12:00:00Z</updated>
  <link rel="enclosure" type="application/octet-stream" href="http://developer.apple.com/docsets/CoreRef2004.xar"/>
  <docset:identifier>com.apple.ADC_Reference_Library.CoreReference</docset:identifier>
  <docset:version>200.4</docset:version>
  <docset:minimumXcodeVersion>3.0</docset:minimumXcodeVersion>
  <docset:signer>CN=ADC DocSet Update,O=Apple Inc.,OU=Apple Developer Connection,C=US</docset:signer>
  <docset:issuer>CN=ADC DocSet Update,O=Apple Inc.,OU=Apple Developer Connection,C=US</docset:issuer>
</entry>
```


New or updated documentation sets are downloaded by Xcode as XAR archives. The documentation set contained in the archive must pass the Xcode security checks described later in this section before Xcode can place the documentation set in the user’s filesystem.

To determine whether an installed documentation set needs to be updated when examining its feed, Xcode performs the following tasks:

1. For each installed documentation set, finds the matching (`docset:identifier`) entry with the highest version number (`docset:version`) that has the same `signer` and `issuer` values and is compatible with the running version of Xcode (`minimumXcodeVersion` and `maximumXcodeVersion`.
2. Compares the version number of the entry with the version number of the installed documentation set to determine if the version number of the entry is higher than the version number of the documentation set. If it is, then the installed documentation set needs to be updated.

When a documentation set that hasn’t been installed on the user’s computer becomes available, the user can download the documentation set by pressing the Get button for that documentation set in Documentation preferences. When an update to an installed documentation set is available, Xcode will update it automatically unless the user opts to do so manually.

To ensure that the documentation set acquisition process is not used as a mechanism to introduce malicious software into a user’s computer, Xcode performs several security checks before unarchiving documentation set archives and placing them in the user’s filesystem. Among these checks are:

- __Documentation set archive signature verification.__ Xcode verifies that the signature used in incoming documentation sets matches the signature of the corresponding web feed or the documentation set being updated.
- __Quarantine of incoming documentation sets.__ Before installing an incoming documentation set, Xcode places it in the user’s private temporary directory in `/var/folders` and marks it as quarantined.
- __Nonexecutable code verification.__ Xcode ensures that the incoming documentation set does not contain executable code.
- __Administrator authentication.__ When installing new documentation sets in privileged locations for the first time or when updating installed documentation sets in privileged locations, Xcode may request administrator authentication before carrying out the install or update process. (When the user has already approved the acquisition of a signed documentation set, further signed updates of the same documentation set do not require administrator authentication.)

The following sections describe the tasks Xcode performs when getting new documentation sets or updating installed documentation sets.

When the incoming documentation set has not been installed in any of the documentation set locations (that is, its identifier doesn’t match the identifier of any installed documentation set), the user can click the Get button next to the documentation set’s name in the documentation set list to install the new documentation set. (The documentation set list is in Documentation preferences.) After the user clicks the button, Xcode performs the following tasks:

1. __Administrator authentication.__ If the documentation set will be installed into a privileged location, Xcode will request administrator authentication. If the user is unable to authenticate as one of the computer’s administrators, Xcode terminates the install process.

   When the documentation set is to be placed in a user-writable location, no authentication is performed.
2. __Signature verification.__ If the web feed provides a signature, Xcode determines whether the signature is valid and whether it matches the incoming documentation set’s signature. If either of these tests is not passed, Xcode terminates the install process.
3. __Installation.__ If a documentation set from the same publisher of the incoming documentation set is installed in any documentation set location, Xcode installs the incoming documentation set in one of those locations. Otherwise, Xcode places the documentation set in `/Library/Developer/Shared/Documentation/DocSets`.
4. __End.__ Xcode ends the process.

An update occurs when the identifier of the incoming documentation set matches the identifier of an _installed documentation set_ (a documentation set in one of the documentation set locations). Xcode replaces the installed documentation set with the incoming one. Xcode performs the following tasks during an update:

1. If the installed documentation set bundle is owned by the `_devdocs` system user and the incoming documentation set is signed:

   1. __Signature verification.__ Xcode determines whether the signature in the incoming documentation set is valid and whether it matches the installed documentation set’s signature. If either of these tests is not passed, Xcode terminates the process.
   2. __Update.__ Xcode replaces the installed documentation set with the incoming one.
   3. __End.__ Xcode ends the process.
2. If the installed documentation set bundle is owned by the `_devdocs` system user and the incoming documentation set is not signed:

   1. __Administrator authentication.__ If the user is unable to authenticate as one of the computer’s administrators, Xcode terminates the process.
   2. __Update.__ Xcode replaces the installed documentation set with the incoming one.
   3. __End.__ Xcode ends the process.
3. If the installed documentation set bundle is writable by the user:

   1. __Update.__ Xcode replaces the existing documentation set with the incoming one.
   2. __End.__ Xcode ends the process.
4. Otherwise, Xcode terminates the process.

Listing 7-3 shows the entire specification for a sample Atom feed. This feed includes two documentation sets, Core Reference Library and PDF 2.0 reference material.

__Listing 7-3__  Example Atom feed

```
<feed xmlns="http://www.w3.org/2005/Atom"
  xmlns:docset="http://developer.apple.com/rss/docset_extensions"
  xml:lang="en">
  <id>http://developer.apple.com/</id>
  <title type="text">Apple Developer Documentation</title>
  <updated>2006-03-24T12:00:00Z</updated>
  <author>
    <name>Apple Developer Publications</name>
    <uri>http://developer.apple.com/</uri>
  </author>
  <rights>Copyright (c) 2007, Apple Inc.</rights>
  <link rel="self" href="ADCDocSets.atom" />
  <entry>
    <id>http://developer.apple.com/docsets/corereflib1.0</id>
    <title type="text">Core Reference Library</title>
    <summary type="text">Includes reference for Cocoa and other frameworks.</summary>
    <updated>2006-03-24T12:00:00Z</updated>
    <!-- Link to actual download. This is required. -->
    <link rel="enclosure" type="application/octet-stream" href="corereflib1.0/corereflib1.0.xar"/>
    <docset:identifier>com.apple.ADC_Reference_Library.CoreReference</docset:identifier>
    <docset:version>1.0</docset:version>
    <docset:minimumXcodeVersion>3.0</docset:minimumXcodeVersion>
  </entry>
  <entry>
    <id>tag:developer.apple.com,2008-04-23:com.apple.ADC_Reference_Library.JavaReference/17</id>
    <title type="text">Java Library</title>
    <summary type="text">Java Library (v17)</summary>
    <updated>2009-01-05T08:51:17-07:00</updated>
    <link rel="enclosure" type="application/octet-stream" href="java/javaref17.xar"></link>
    <docset:identifier>com.apple.ADC_Reference_Library.JavaReference</docset:identifier>
    <docset:version>17</docset:version>
    <docset:minimumXcodeVersion>3.1</docset:minimumXcodeVersion>
  </entry>
</feed>
```

[Next](Testing%20and%20Packaging%20Documentation%20Sets.md)[Previous](Internationalizing%20Documentation%20Sets.md)

