---
title: Dictionary Services Programming Guide
apple_id: TP40006152
resource_type: Guide
platform: macOS
topic: User Experience
technology: CoreServices
published: '2007-05-30'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/DictionaryServicesProgGuide/prepare/prepare.html
archived_at: '2026-07-18T02:11:24.394901Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dictionary Services Programming Guide](Introduction.md)


[Next](Accessing%20Dictionaries.md)[Previous](Dictionary%20User%20Interface%20and%20Markup.md)

# Creating Dictionaries

Prior to building a dictionary, you need to create your dictionary source file, prepare a style sheet, edit the property list file, and add any resources needed by your dictionary. This chapter explains how to perform these tasks, provides instructions for building your dictionary, and shows a few simple examples. You’ll also find out how to create a Japanese dictionary, set up preferences, and add front and back matter.

Before you start preparing your source data, copy the `project_template` folder from the development kit to the directory that you use for code development. Then, follow the instructions described in the following sections:

1. [Preparing Dictionary Contents](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjsfvbuqmznknltc)
2. [Editing the Property List File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjsfvbuqmznknlte)
3. [Adding Resources Needed by Your Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjsfvbuqmznknltg)
4. [Preparing the Makefile](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjsfvbuqmznknlti)

Take a look at the `MyDictionary.xml` file provided in the project template. Your dictionary should follow this form, using UTF-8 encoding. You can change the file name to something other than `MyDictionary`, but if you change the name, you must edit the `DICT_SRC_PATH` variable in the makefile.

[Dictionary User Interface and Markup](Dictionary%20User%20Interface%20and%20Markup.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjsfvbuqnbnknltc) ) describes the XML schema you should use to develop a dictionary. The schema uses the RELAX NG schema language, which is described on this website:

[http://www.relaxng.org/](http://www.relaxng.org/)

You should validate your dictionary source prior to building a new dictionary You can use RELAX NG validators programs, which are available from this website:

[http://www.relaxng.org/#validators](http://www.relaxng.org/#validators)

You can also validate XML using jing as follows:

```
$ java -jar <path to jing.jar> <schema definition> <XML to validate>
```

From the project_template folder, with jing located in ../jing/, the command line is as follows:

```
$ java -jar ../jing/bin/jing.jar ../documents/DictionarySchema/AppleDictionarySchema.rng MyDictionary.xml
```

For more information on jing, see:

[http://www.thaiopensource.com/relaxng/jing.html](http://www.thaiopensource.com/relaxng/jing.html)

You can prepare a style sheet to use for the contents of the dictionary by editing the `MyDictionary.css` file provided with the project template. If you change the name of this css file, you need to edit the `CSS_PATH` variable in the makefile.

You should minimally edit the style sheet.  The Dictionary application and the Dictionary window control use their own style definitions to ensure that the contents fit the display. For best results, do not specify an absolute font or font size.

The property list file for a dictionary is an an XML text file. The project template contains an example file—`MyInfo.plist`—whose contents are shown in Listing 2-1. You can edit this file so that it contains entries appropriate for your dictionary. [Table 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjsfvbuqmznknltm) explains the values that you need to provide for your dictionary.

__Listing 2-1__  An example of a property list file for a dictionary

```
<key>CFBundleDevelopmentRegion</key>
<string>English</string>
<key>CFBundleDisplayName</key>
<string>My Dictionary</string>
<key>CFBundleIdentifier</key>
<string>com.apple.dictionary.MySample</string>
<key>CFBundleName</key>
<string>MyDictionary</string>
<key>CFBundleShortVersionString</key>
<string>1.0</string>
<key>DCSDictionaryCopyright</key>
<string>Copyright (c) Apple Computer, Inc.</string>
<key>DCSDictionaryManufacturerName</key>
<string>Apple Computer, Inc.</string>
```

If you change the name of the property list file, you must edit the `PLIST_PATH` variable in the makefile.

__Table 2-1__  Keys and values for the dictionary property list file

| Key | Value |
| `CFBundleDevelopmentRegion` | A region |
| `CFBundleDisplayName` | The full display name of the dictionary. The default is to use the file system name. |
| `CFBundleIdentifier` | The identifier of the dictionary bundle; specify a unique ID. |
| `CFBundleName` | The short display name of the dictionary. |
| `CFBundleShortVersionString` | The version of the dictionary. |
| `DCSDictionaryCopyright` | The copyright notice of the dictionary. |
| `DCSDictionaryManufacturerName` | The manufacturer name of the dictionary. |

You must place any resources (for example, images) that your dictionary needs in the OtherResources folder in the `project_template` folder. When you build the dictionary, the resources are copied into the built dictionary.

For example, if your dictionary uses an image file name `test.png`, you need to place it in the following location:

`project_template/OtherResources/Images/test.png`

The Images folder is copied into the dictionary. When the dictionary needs the image, it uses to the relative path—`Images/test.png`—which is written to the XML file during the build process.

Name your dictionary and then edit the `DICT_NAME` variable in the makefile. This name is used as the folder name for the dictionary. For example, when `DICT_NAME = “My Dictionary”`, the built dictionary is `My Dictionary.dictionary`.

If you change the location of the Dictionary Development Kit from /`Developer/Extras/Dictionary Development Kit`, you must modify the `DICT_BUILD_TOOL_DIR` variable in the makefile to reflect the change.

To build your dictionary, follow these steps:

1. Launch the Terminal application.
2. Use the `cd` command to change to the appropriate location:

   `/Developer/Extras/Dictionary Development Kit`
3. Enter `make`.
4. After the make process finishes successfully, type make install to copy the new dictionary to:

   `~/Library/Dictionaries/`

After running the `make install` command, you can delete all the intermediate files in the objects folder. In the Terminal window, enter make clean to remove the objects folder.

Now you can launch the Dictionary application and test your new dictionary.

As you can see from looking at the makefile, the building process uses a script `build_dict.sh`, located in `/Developer/Extras/Dictionary Development Kit/bin`. This script takes 4 arguments—`dictionary_name`, `dictionary_source_path`, `StyleSheet_path`, and `InfoPlist_path`. It builds a new directory in the `/objects` folder.

Yomi shows a simple example of a dictionary that contains an entry for the word _make_. It looks like Figure 1-1 when opened using the Dictionary application.

__Listing 2-2__  A one-word dictionary

```xml
<?xml version="1.0" encoding="UTF-8"?>
<d:dictionary xmlns="http://www.w3.org/1999/xhtml" xmlns:d="http://www.apple.com/DTDs/DictionaryService-1.0.rng">
<d:entry id="make_1">
    <d:index d:value="make" d:title="make"/>
    <d:index d:value="makes" d:title="makes (make)"/>
    <d:index d:value="made" d:title="made (make)"/>
    <d:index d:value="making" d:title="making (make)"/>
    <h1>make</h1><span class="syntax">| māk |</span>
    <div>
        <ol>
            <li>
                Form by putting parts together or combining substances; construct; create; produce
                <span d:priority="2"> : <i>Mother made her a beautiful dress</i>
                </span>
                .
            </li>
            <li>
                Cause to be or become
                <span d:priority="2"> : <i>The news made me happy</i>
                </span>
                .
            </li>
        </ol>
    </div>
    <div d:parental-control="1" d:priority="2">
        <h3>PHRASES</h3>
        <div id="make_it"><b>make it</b> : succeed in something; survive.</div>
        <h4><a href="x-dictionary:r:make_up_ones_mind"><b>make up one's mind</b></a></h4>
    </div>
</d:entry>
</d:dictionary>
```


Listing 2-3 shows how to tag the following content to create an acronym dictionary.

- LDAP, Lightweight Directory Access Protocol
- MIDI, Musical Instrument Digital Interface
- XML, Extensible Markup Language

__Listing 2-3__  An acronym dictionary

```xml
<?xml version="1.0" encoding="UTF-8"?>
<d:dictionary xmlns="http://www.w3.org/1999/xhtml" xmlns:d="http://www.apple.com/DTDs/DictionaryService-1.0.rng">
<d:entry id="ldap">
    <d:index d:value="LDAP" d:title="LDAP"/>
    <h1>LDAP</h1>
    <p>Lightweight Directory Access Protocol</p>
</d:entry>
<d:entry id="midi">
    <d:index d:value="MIDI" d:title="MIDI"/>
    <h1>MIDI</h1>
    <p>Musical Instrument Digital Interface</p>
</d:entry>
<d:entry id="xml">
    <d:index d:value="XML" d:title="XML"/>
    <h1>XML</h1>
    <p>Extensible Markup Language</p>
</d:entry>
</d:dictionary>
```


You can add front and back matter to a dictionary by following these steps:

1. [Prepare an Entry for the Front and Back Matter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjsfvbuqmznknltcoa)
2. [Modify the Info.plist File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjsfvbuqmznknltcoi)
3. [Add an Index Entry (Optional)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjsfvbuqmznknltema)

You can view the front and back matter for a dictionary using the Dictionary application. In the Go menu, choose Front/Back Matter.

In the XML file for the dictionary, you need to specify a front-back matter entry using an `id` attribute whose value is set to `front_back_matter` as shown in the following simple example:

```
<d:entry id="front_back_matter" d:title="Front/Back Matter">
    <h1><b>My Dictionary</b></h1>
    <h2>Front/Back Matter</h2>
    <p>
        This is a front matter page of the sample dictionary.<br/>
    </p>

    ...

</d:entry>
```


You must modify the property list for the dictionary by adding the `DCSDictionaryFrontMatterReferenceID` key to the `Info.plist` file. The associated value is a string that specifies the `id` value you used in the XML file. The following shows the string used in [Prepare an Entry for the Front and Back Matter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjsfvbuqmznknltcoa).

```
<key>DCSDictionaryFrontMatterReferenceID</key>
<string>front_back_matter</string>
```


This example does not use a `<d:index>` element, which means that the page won’t show up in a search. If you want the front and back matter to show in a search, add the`<d:index>` element. Otherwise, users can view the front and back matters by choosing Go > Front/Back Matter from within the Dictionary application.

You have the option to set up preferences for a dictionary. Users access the preferences settings from within the Dictionary application by choosing Dictionary > Preferences. For example, the New Oxford American Dictionary provided with OS X v10.5 allows users to choose from among three phonetic notations—U.S. English (Diacritical), U.S. English (IPA), or British English (IPA).

This section shows how you can set up preferences for your dictionary. You can find the files associated with this example in the Dictionary Development Kit located in:

`/Developer/Extras/Dictionary Development Kit/samples/`

To implement dictionary-specific preferences, follow these steps:

1. [Modify the Dictionary Contents Appropriately](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjsfvbuqmznknltcna).
2. [Prepare an XSLT File to Apply to Dictionary Entries](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjsfvbuqmznknltcni).
3. [Implement the Preferences User interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjsfvbuqmznknltcnq).
4. [Modify the Info.plist File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjsfvbuqmznknltcny).

You need to modify the contents to support the preferences that you set up. For example, if you want to allow the user to choose from among three phonetic notations, you need to provide the three phonetic notations for each entry in our dictionary. The following example shows three phonetic notations for the word `make`.

```
<d:entry id="make_1" d:title="make">
    ...
    <h1>make</h1>
    <span class="syntax">
        <span d:pr="US">| māk |</span>
        <span d:pr="US_IPA">| meɪk |</span>
        <span d:pr="UK_IPA">| meɪk |</span>
    </span>
    ...
</d:entry>
```

Note that the XML does not specify which phonetic notation to show. You’ll do that in the next section by creating an XSLT file.

The XSLT files contains instructions that Dictionary Services applies to each entry before displaying the it. In this example, you need to provide instructions to remove the unused phonetic notation. For this, use the `$pronunciation` variable, which is a global variable supply by the Dictionary application, as shown in the following example.

```
<xsl:template match="*[@d:pr='US']">
    <xsl:if test="$pronunciation = '0'">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()" />
        </xsl:copy>
    </xsl:if>
</xsl:template>

<xsl:template match="*[@d:pr='IPA']">
    <xsl:if test="$pronunciation = '1'">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()" />
        </xsl:copy>
    </xsl:if>
    <xsl:if test="$pronunciation = '2'">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()" />
        </xsl:copy>
    </xsl:if>
</xsl:template>

<xsl:template match="*[@d:pr='US_IPA']">
    <xsl:if test="$pronunciation = '1'">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()" />
        </xsl:copy>
    </xsl:if>
</xsl:template>

<xsl:template match="*[@d:pr='UK_IPA']">
    <xsl:if test="$pronunciation = '2'">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()" />
        </xsl:copy>
    </xsl:if>
</xsl:template>
```


You need to provide an XHTML file that specifies the user interface to present in the Dictionary Preferences window in the Dictionary application. The following example shows how to set up preferences for phonetic notation. The user will see three choices displayed as radio buttons. After making a selection, Dictionary Services saves the it and passes the selection to the XSLT instructions. The instructions are then applied to the dictionary entries.

```
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    </head>
    <body>
        <div id="copyright"></div>
        <hr />
        <div class="query">
            <input type="hidden" name="version" value="1" />
        </div>
        <div class="query">
            Pronunciation:<br />
            <input type="radio" name="pronunciation" value="0">US English (Diacritical)</input><br />
            <input type="radio" name="pronunciation" value="1">US English (IPA)</input><br />
            <input type="radio" name="pronunciation" value="2">British English (IPA)</input><br />
        </div>
    </body>
</html>
```


You must add keys to the `Info.plist` file to indication that the dictionary has its own preferences. The values for this example are shown in the following property list entry. You need to change the values to ones that are appropriate for your dictionary. The values expected for each of the keys are shown in [Table 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjsfvbuqmznknltcmq).

```
<key>DCSDictionaryDefaultPrefs</key>
    <dict>
        <key>pronunciation</key>
        <string>0</string>
        <key>version</key>
        <string>1</string>
    </dict>
    <key>DCSDictionaryPrefsHTML</key>
    <string>MyDictionary_prefs.html</string>
    <key>DCSDictionaryXSL</key>
    <string>MyDictionary.xsl</string>
```


__Table 2-2__  Values for dictionary preferences keys

| Key | Value |
| `DCSDictionaryDefaultPrefs` | None. This key specifies that key-value pairs for the default values follow. |
| `DCSDictionaryPrefsHTML` | The XHTML file name |
| `DCSDictionaryXSL` | The XSLT file name |

The Japanese language has multiple character classes—Hiragana, Katakana, and Kanji. Because of this, Japanese words often have multiple representations. Kanji uses ideographic characters; Hiragana and Katakana use phonograms. (Foreign words are often represented using Katakana. Roman characters also are used.) A Kanji word has its Yomi that represents its reading. Hiragana or Katakana usually describe Yomi.

Entries in many Japanese word dictionaries are sorted by Yomi. In such dictionaries, the user enters Yomi to search for words. Using Yomi for Hiragana and Katakana is not an issue because these are phonograms, and there aren’t many of them. But for Kanji, it is an issue because the same Yomi can represent different Kanji. For example the Yomi "かい" represents many words: 会, 界, 貝, 解, 階, 回, 介, ...下位, 甲斐, ...

A user who searches for "かい" gets these results:

- かい 【会】
- かい 【界】
- かい 【貝】
- かい 【解】
- かい 【階】
- かい 【回】
- かい 【介】
- ...
- かい 【下位】
- かい 【甲斐】
- ...

The user can choose the appropriate entry using the additional Kanji part.

If the search word is "くふう", the results are:

- くふう 【工夫】
- くふう 【句風】

Here are search results for “工夫" . The Yomi くふう and こうふ are added to choose appropriate entry.

- 工夫 【くふう】
- 工夫 【こうふ】

You need to mark Yomi content in your Japanese dictionary using the `d:yomi` attribute. The Dictionary application displays the `d:title` and `d:yomi` in the appropriate order in the search results list. When the user searches using Hiragana, the Yomi appears before the Kanji. When the user searches using Kanji, the Yomi is added.

For the words in a Japanese dictionary that have multiple representations, the value associated with the `d:title` element can be different from the value associated with the `d:value` element. To ensure that users can find what they search for, use the `d:yomi` attribute with the `d:index` element.

In a Japanese dictionary, a Kanji entry has both Kanji and Yomi as its `d:value` attribute of the `d:index` element. The `d:title` markup in its ordinary form is:

```
<d:entry ... d:title="工夫">
    <d:index d:value="くふう" d:title="工夫"/>
    <d:index d:value="工夫" d:title="工夫"/>
    ...
</d:entry>
```

You can add Yomi using the `d:yomi` attribute as shown:

```
<d:entry ... d:title="工夫">
    <d:index d:value="くふう" d:title="工夫" d:yomi="くふう"/>
    <d:index d:value="工夫" d:title="工夫" d:yomi="くふう"/>
    ...
</d:entry>
<d:entry ... d:title="工夫">
    <d:index d:value="こうふ" d:title="工夫" d:yomi="こうふ"/>
    <d:index d:value="工夫" d:title="工夫" d:yomi="こうふ"/>
    ...
</d:entry>
```

The Dictionary application uses `d:yomi` and `d:title` to add supplementary information either for searching by Yomi or searching by Kanji. You can omit `d:title` when it has the same value as `d:value`.

The Dictionary Development Kit contains the source for a sample Japanese dictionary (see `/Developer/Extras/Dictionary Development Kit/samples/`). The dictionary contains entries for various cases, including the following:

- A word that is written using multiple, mixed character classes.
- A foreign word that has both Katakana and Roman representations.

[Next](Accessing%20Dictionaries.md)[Previous](Dictionary%20User%20Interface%20and%20Markup.md)

