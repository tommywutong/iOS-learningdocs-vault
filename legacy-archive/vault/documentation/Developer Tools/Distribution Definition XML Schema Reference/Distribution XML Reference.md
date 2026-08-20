---
title: Distribution Definition XML Schema Reference
apple_id: TP40005370
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/DistributionDefinitionRef/Chapters/Distribution_XML_Ref.html
archived_at: '2026-07-15T07:30:58.564540Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Distribution Definition XML Schema Reference](About%20Distribution%20Definition%20Files.md)


[Next](Document%20Revision%20History.md)[Previous](About%20Distribution%20Definition%20Files.md)

# Distribution XML Reference

Defines OS version requirements. These consist of one or more version ranges, specified as `os-version` elements. The version of the operating system on the target volume must fall into one of these ranges to allow installation.

None.

Available in OS X v10.6.6 and later.

This element can contain the following element:

- [os-version](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvztgq) (one or more): The supported OS versions.

Identifies an application that must be closed before the package is installed.

| Attribute name | Type | Description |
| --- | --- | --- |
| `id` | String | _Required._ The bundle identifier of the application. |

None.

_Reserved._

Defines a background image for the Installer.

| Attribute name | Type | Description |
| --- | --- | --- |
| `alignment` | String | _Optional._ The alignment used to render the background image. Values: `center` (default), `left`, `right`, `top`, `bottom`, `topleft`, `topright`, `bottomleft`, and `bottomright`.  Only used by the Installer. |
| `file` | String | _Required._ The filename of an image in the distribution package—for example, `background.png` or `./background.png`. |
| `mime-type` | String | The standard MIME type of the image. |
| `scaling` | String | _Optional._ The scaling used to render the background image. Values: `tofit` (default), `none`, and `proportional`. |
| `uti` | String | The UTI type of the image. This attribute is provided because some file types don’t have a MIME type. |

None.

Defines a single bundle. The meaning of this element differs considerably depending on its parent element; see the parent element’s documentation for details.

| Attribute name | Type | Description |
| --- | --- | --- |
| `CFBundleShortVersionString` | String | _Optional._ The short version string of the bundle, as defined in its `Info.plist` file. |
| `CFBundleVersion` | String | _Optional._ The bundle’s version, as defined in its `Info.plist` file. |
| `id` | String | _Required._ The identifier of the bundle—that is, the value of `CFBundleIdentifier` in the bundle’s `Info.plist` file. |
| `path` | String | _Required._ The path at which the bundle is installed, relative to where the package is installed. For example, `Applications/Sample.app`. |
| `search` | Boolean | _Optional._ Indicates whether to search for the bundle by its identifier if it is not found at the given path. Values: `false` (default), `true`.  Only valid when this element is a child of a `required-bundles` element. |
| `BuildVersion` | - | _Reserved._ |
| `SourceVersion` | - | _Reserved._ |

None.

Defines the version of the bundles delivered by the parent element. You do not typically specify this element; `productbuild` inserts it from the actual package data when the product archive is created.

None.

Available in OS X v10.6.6 and later.

This element can contain the following elements:

- [bundle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvztgy) (one or more): The package-relative path and version strings of the bundles installed.

Defines an installation choice of a distribution package.

| Attribute name | Type | Description |
| --- | --- | --- |
| `customLocation` | Absolute file path | _Optional._ Specifies the default installation location, within the installation volume, for this choice. Implies that the user can choose a different installation location. If unspecified, the user cannot choose the installation location for this choice. |
| `customLocationAllowAlternateVolumes` | Boolean | Optional if `customLocation` is specified; otherwise, not allowed. Specifies whether the user can choose the installation volume. Values: `false` (default) indicates that the user can choose a different location than what is given by `customLocation` but cannot change the volume; `true` indicates that the user can choose the installation volume and the location on that volume. A value of `true` is only valid for packages that use the Installer. |
| `description` | String, localization key | Required for packages that use the Installer; otherwise, optional. Specifies the description of the installation choice. Localizable. |
| `description-mime-type` | String | _Optional._ The MIME type of the text data in the `description` attribute. Values: `text/plain` (default), `text/rtf`, or `text/html`. |
| `enabled` | Boolean JavaScript expression | _Optional._ Specifies whether the user can select or deselect this option in the Installer customization pane. If `false`, or a JavaScript expression that evaluates to `false`, the choice is dimmed so the user cannot select or deselect it. Re-evaluated as the user interacts with the choice tree, so a choice can be enabled or disabled based on the state of other choices. Default value is `true`. |
| `id` | String | _Required._ Unique identifier of the installation choice, used to bind this element to the `line` element that determines its position in the installation-choice hierarchy.  Must match the `choice` attribute of exactly one `line` element. |
| `selected` | Boolean JavaScript expression | _Optional._ Specifies whether this option is selected or deselected for installation. If `false`, or a JavaScript expression that evaluates to `false`, the choice will not be installed. In general, you should not declare this attribute on a choice that is visible and enabled, because it can interfere with the user’s selections. Default value is `true`. |
| `start_enabled` | Boolean | _Optional._ Specifies whether this option is initially enabled in the Installer customization pane. Values: `true` (default), or `false`. |
| `start_selected` | Boolean | _Optional._ Specifies whether this option is initially selected or deselected for installation. Values: `true` (default), or `false`. |
| `start_visible` | Boolean | _Optional._ Specifies whether this option is initially visible in the Installer customization pane. Values: `true` (default), or `false`. |
| `title` | String, localization key | _Required._ Specifies the title of the installation choice. Localizable. |
| `visible` | Boolean JavaScript expression | _Optional._ Specifies whether this option is visible in the Installer customization pane. If `false`, or a JavaScript expression that evaluates to `false`, the choice is hidden from the user. Default value is `true`.  Avoid making choices appear and disappear while the user is interacting with the installation process. This provides a poor user experience. |
| `bundle` | - | _Reserved._ |
| `customLocationIsSelfContained` | - | _Reserved._ |
| `tooltip` | - | _Reserved._ |
| `versStr` | - | _Reserved._ |

This element can contain the following element:

- [pkg-ref](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzrge) (zero or more): The choice’s packages. You should only associate packages with a choice that has no subchoices (as defined by the hierarchy of `line` elements).

Defines the installation-choice hierarchy of a distribution package.

| Attribute name | Type | Description |
| --- | --- | --- |
| `ui` | - | _Reserved._ |

This element can contain the following element:

- [line](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzz) (one or more): The top-level installation choices.

Specifies text that is displayed by Installer at the end of the installation process.

| Attribute name | Type | Description |
| --- | --- | --- |
| `file` | String | _Required._ The filename of the conclusion file in the distribution package—for example, `conclusion.rtf`. |
| `mime-type` | String | The MIME-type specifier for the data contained in the file. |
| `uti` | String | The UTI-type specifier for the data contained in the file. |
| `language` | - | _Reserved._ |

None.

Indicates what domains the package may be installed into. If this element is not present, `enable_anywhere` is `true`, `enable_currentUserHome` is `false`, and `enable_localSystem` is `true`.

| Attribute name | Type | Description |
| --- | --- | --- |
| `enable_anywhere` | Boolean JavaScript expression | _Required._ If `true`, or a JavaScript expression that evaluates to `true`, the product can be installed at the root of any volume, including nonsystem volumes. Otherwise, it cannot be installed at the root of a volume. |
| `enable_currentUserHome` | Boolean JavaScript expression | _Required._ If `true`, or a JavaScript expression that evaluates to `true`, the product can be installed into the current user’s home directory. Otherwise, it cannot be installed in the current user’s home directory.  A home directory installation is done as the current user (not as `root`), and it cannot write outside of the home directory. You should enable this only if the product can be installed in the user’s home directory and be completely functional from that location. |
| `enable_localSystem` | Boolean JavaScript expression | _Required._ If `true`, or a JavaScript expression that evaluates to `true`, the product can be installed into the root directory. This attribute should usually be `true` unless the product can be installed only to the user’s home directory. |

None.

Specifies whether the installation host meets the distribution’s system requirements. The installation check passes if the script returns `true`, any RAM requirements are met, and any graphics requirements are met.

| Attribute name | Type | Description |
| --- | --- | --- |
| `script` | Boolean JavaScript expression | _Optional._ Specifies whether the requirements are met. If `true` (default), or a Boolean JavaScript expression that evaluates to `true`, the installation proceeds, subject to the other checks.  If the script evaluates to `false`, it must also set `my.result.type` and `my.result.message` to indicate the severity of the problem and provide a message to display. If `my.result.type` is `Warning`, the installation may be allowed to proceed after informing the user. |

This element can contain the following elements:

- [ram](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzrg4) (zero or one): The required RAM.
- [required-graphics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzrhe) (zero or one): The GPU requirements.

The root element of the distribution definition. All other elements in the distribution definition file are children of this element.

| Attribute name | Type | Description |
| --- | --- | --- |
| `minSpecVersion` | Integer | _Required._ The schema version of a distribution file. Use `1` for the version used prior to OS X v10.6.6, or `2` after that. |
| `maxSpecVersion` | - | _Reserved._ |
| `verifiedSpecVersion` | - | _Reserved._ |

This element can contain the following elements:

- [background](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzs) (zero or one)
- [choice](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzrga) (one or more)
- [choices-outline](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzy) (exactly one)
- [conclusion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzw) (zero or one)
- [domains](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvztgu) (zero or one)
- [installation-check](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzrgi) (zero or one)
- [license](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzv) (zero or one)
- [locator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzrgu) (zero or more)
- [options](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzx) (zero or one)
- [pkg-ref](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzrge) (one or more)
- [product](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzxgm) (zero or one)
- [readme](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzu) (zero or one)
- [script](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzrgq) (zero or one)
- [title](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzr) (exactly one)
- [volume-check](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzrgm) (zero or one)
- [welcome](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzt) (zero or one)

Specifies text that is displayed by Installer during the installation process.

| Attribute name | Type | Description |
| --- | --- | --- |
| `file` | String | _Required._ The filename of the welcome file in the distribution package—for example, `welcome.rtf`. |
| `mime-type` | String | The MIME-type specifier for the data contained in the file. |
| `uti` | String | The UTI-type specifier for the data contained in the file. |
| `auto` | - | _Reserved._ |
| `language` | - | _Reserved._ |
| `sla` | - | _Reserved._ |

None.

Defines where a choice fits into the installation-choice hierarchy of a distribution package.

| Attribute name | Type | Description |
| --- | --- | --- |
| `choice` | String | _Required._ Identifies the installation choice associated with this node of the installation-choice hierarchy of a distribution package. The value must match the ID of a `choice` element. See [choice](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzrga).  Do not reference the same ID from more than one line element, not even from different `installation-choice` hierarchies; if you do so, the behavior is undefined. |

This element can contain the following element:

- [line](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzz) (zero or more): The subchoices of this choice.

_Reserved._

Defines a search rule for finding software that is already installed on the system.

None.

This element can contain the following element:

- [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvztg4) (one or more): The search rule.

Identifies applications that must be closed before the package is installed.

Applications are considered only if the package that contains this element has been selected for installation.

None.

This element can contain the following element:

- [app](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzsge) (one or more): The applications.

Specifies the installation properties of a package within the distribution.

| Attribute name | Type | Description |
| --- | --- | --- |
| `allow-external-scripts` | Boolean | _Optional._ Specifies whether the [run](https://developer.apple.com/documentation/installerjs/system/1812364-run) and [runOnce](https://developer.apple.com/documentation/installerjs/system/1812367-runonce) JavaScript functions can be executed. Values: `false` (default) or `true`. For information about these functions, see System in _[Installer JavaScript Reference](https://developer.apple.com/documentation/installerjs)_. |
| `customize` | String | _Optional._ Specifies whether the user can customize the installation by selecting or deselecting installation choices. Values:  `allow` (default) gives the user an opportunity to customize the installation, `always` presents the customization view automatically.  `never` does not provide access to the customization view. |
| `hostArchitectures` | String | _Optional._ A comma-separated list of supported architecture codes. Valid codes are `i386`, `x86_64`, and `ppc`. Note that `i386` matches both 32-bit and 64-bit systems, but `x86_64` matches only 64-bit systems. |
| `mpkg` | String | _Optional._ Identifies a package (`pkg-ref` element) whose installation operations must be performed as part of the installation of this distribution.  Deprecated. |
| `require-scripts` | Boolean | _Optional._ Indicates whether the distribution uses JavaScript code. Values: `true` (default) or `false`. If this value is `false`, all attributes whose value may be a JavaScript expression must be set to either `true` or `false`.    Available in OS X v10.6.6 and later. |
| `rootVolumeOnly` | Boolean | _Optional._ Specifies whether the user can choose an installation volume other than the boot volume. Values: `true` or `false`.  Deprecated. Use domains instead. |
| `type` | - | _Reserved._ |
| `visibleOnlyForPredicate` | - | _Reserved._ |

None.

Defines a range of supported OS versions.

This element is designed for you to use a specific OS version number for the `min` attribute, and a major OS version number for the `before` attribute. The expectation is that you will know an exact minimum version but not an exact major version. This keeps you from having to guess the last minor revision before the next major revision, as you would have to do if the `before` attribute were inclusive.

| Attribute name | Type | Description |
| --- | --- | --- |
| `before` | String | _Optional._ The maximum allowed version (exclusive). If the OS version is greater than or equal to this version, installation will be disallowed (unless the OS falls in the range of another `os-version` element). If no value is given, there is no upper bound on the range—any version newer than the minimum is allowed. |
| `min` | String | _Required._ The minimum allowed version (inclusive). If the OS is less than this version, installation will be disallowed (unless the OS falls in the range of another `os-version` element). |

None.

References a component package that can be installed.

| Attribute name | Type | Description |
| --- | --- | --- |
| `active` | Boolean JavaScript expression | _Optional._ Indicates whether the package is installed. Values: `true` (default), `false`.  If `false`, or a JavaScript expression that evaluates to false, the package is not installed, even if its associated choice was selected.  This provides an additional way to activate and deactivate packages. It overrides the setting on the parent element. |
| `auth` | String | Defines the authorization level needed to install this package. Values: `none` or `root`.  Deprecated. The installation domain determines the necessary authorization level. |
| `id` | String | _Required._ Uniquely identifies a component package within a distribution package—for example, `com.apple.TextEdit.pkg`. The value of this attribute is usually the same as the component package’s identifier, but it is not required to be the same.  If there are multiple `pkg-ref` elements with the same ID, their attributes will be collapsed together as if they were specified with a single element. In particular, a `pkg-ref` element with only an ID can be used inside of a `choice` element to bind that choice to a `pkg-ref` that is more fully defined elsewhere in the distribution file. |
| `installKBytes` | Integer | _Optional._ Specifies the size of the package’s payload in kilobytes.  You typically omit this attribute because `productbuild` sets it from the actual package when the product archive is created. |
| `onConclusion` | String | _Optional._ Specifies the action to take after the installation has finished. Values, from lowest to highest: `None` (default), `RequireLogout`, `RequireRestart`, or `RequireShutdown`.  The Installer takes the highest value from all enabled packages and requires the associated action. |
| `onConclusionScript` | String | _Optional._ A JavaScript expression that evaluates to one of the string values expected for `onConclusion`. If this attribute is present, any `onConclusion` attribute is ignored.  Available in OS X v10.7 and later. |
| `version` | String | _Required._ Specifies the version of the package’s payload.  You typically omit this attribute because `productbuild` will set it from the actual package when the product archive is created. |
| `archiveKBytes` | - | _Reserved._ |
| `packageIdentifier` | - | _Reserved._ |

_Required._ A URL specifying the location of the installation package to which this element refers. Typically, you specify a simple filename and `productbuild` adjusts the URL as needed when the product archive is created. If you define multiple `pkg-ref` elements with the same ID, exactly one of them should have text content.

This element can contain the following elements:

- [must-close](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzxg4) (zero or one): The application(s) to be closed before installing this package.
- [bundle-version](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzwgi) (zero or one): The bundle version.
- [relocate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzyg4) (zero or more): The information to support relocatable bundles.

To provide a `must-close` element, add a separate `pkg-ref` element with the same ID to contain the `must-close` element. For example:

```
<pkg-ref id="abc">x.pkg</pkg-ref>
<pkg-ref id="abc">
   <must-close>
      <app id="com.example.MyApp"/>
   </must-close>
</pkg-ref>
```


Defines a top-level product identifier and version. Used for distributing via the App Store.

| Attribute name | Type | Description |
| --- | --- | --- |
| `id` | String | _Required._ The top-level product identifier. The value should be the same as the bundle identifier of the contained application. |
| `version` | String | _Required._ The version string for the top-level product. The value should be the same as the short version string of the contained application. |

Available in OS X v10.6.6 and later.

None.

Specifies the minimum amount of RAM that the system must have.

| Attribute name | Type | Description |
| --- | --- | --- |
| `min-gb` | String | _Required._ The minimum required RAM in gigabytes.  (Consistent with how sizes are displayed in OS X v10.6 and later, a gigabyte is defined as 109 bytes, not 230 bytes.) |

Available in OS X v10.6.6 and later.

None.

Specifies text that is displayed by Installer during the installation process.

| Attribute name | Type | Description |
| --- | --- | --- |
| `file` | String | _Required._ The filename of the readme file in the distribution package. For example, `readme.rtf`. |
| `mime-type` | String | The MIME-type specifier for the data contained in the file. |
| `uti` | String | The UTI-type specifier for the data contained in the file. |
| `language` | - | _Reserved._ |

None.

Describes a relocatable bundle. Relocatable bundles allow the user to install an upgrade in the same path as the current version. The path is located by the `search` element whose ID is specified by the `search-id` attribute. The bundle is specified by the child `bundle` element. For example, application bundles are typically relocatable.

| Attribute name | Type | Description |
| --- | --- | --- |
| `search-id` | String | _Required._ Specifies the ID of the `search` element whose results are applied to the bundle that is this element’s child element.  If the search returns `false`, the relocate does nothing. If the search returns an array of results, the first result is used. |

This element can contain the following element:

- [bundle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvztgy) (exactly one): The bundle (within the package) that will be installed at the path. The only required attribute for this `bundle` element is its ID.

Specifies bundles that must be already installed on the system.

If the child `bundle` element has a version specified, this is interpreted as the minimum supported version for that bundle. It may also have its `search` attribute set to `true`, indicating that the bundle should be located by its identifier if it doesn’t exist at the specified path.

| Attribute name | Type | Description |
| --- | --- | --- |
| `all` | Boolean | _Optional._ Values: `true` (default) to require all of the specified bundles, or `false` to require at least one of them. |
| `description` | String, localization key | _Optional._ A description of the required bundles, displayed to the user if the requirement is not met. |

This element can contain the following element:

- [bundle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvztgy) (one or more): The required bundles.

Specifies requirements that must be met by at least one OpenCL device.

None.

Available in OS X v10.7 and later.

The predicate, as a string. For details about the predicate format, see the `productbuild` man page.

To prevent characters in the predicate from being interpreted by the XML parser, mark it as CDATA content.

Specifies requirements that must be met by at least one OpenGL hardware renderer.

None.

Available in OS X v10.6.8 and later.

The predicate, as a string. For details about the predicate format, see _[Specifying required OpenGL capabilities for the Mac App Store](https://developer.apple.com/library/archive/qa/qa1748/_index.html#//apple_ref/doc/uid/DTS40011181)_ and the `productbuild` man page.

To prevent characters in the predicate from being interpreted by the XML parser, mark it as CDATA content.

Specifies GPU requirements.

| Attribute name | Type | Description |
| --- | --- | --- |
| `description` | String, localization key | _Optional._ A description of the graphics requirement. Localizable.  If no description is specified, a generic message is used. It is generally best to use the generic message unless the requirements are very straightforward. |
| `single-device` | Boolean | _Optional._ Values: `false` (default) to allow the OpenCL and OpenGL requirements to be met by different devices, or `true` to require a single device to simultaneously meet both requirements. |

This element can contain the following elements:

- [required-cl-device](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzvgi) (zero or one): The OpenCL requirements.
- [required-gl-renderer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzwgy) (zero or one): The OpenGL requirements.

Defines a set of JavaScript functions.

| Attribute name | Type | Description |
| --- | --- | --- |
| `language` | - | _Reserved._ |

JavaScript code, typically the definition of functions called from attributes of other elements.

To prevent characters in the script from being interpreted by the XML parser, mark it as CDATA content:

```
<script>
<![CDATA[
// ... JavaScript ...
]]>
</script>
```

If you choose not to mark your script as CDATA content, you must take great care to properly escape all characters that have special meaning in XML markup.

Defines a search rule for finding installed software. The result should be used by another search rule or bound to a bundle via a `relocate` element.

| Attribute name | Type | Description |
| --- | --- | --- |
| `id` | String | _Required._ Uniquely identifies the search; used in the `search-id` attribute of other elements to reference this search. |
| `script` | String | Required if `type` is `script`; otherwise, not allowed.  A JavaScript expression that evaluates to `false`, a path as a string, or an array of paths. If it returns an array of paths, the first one is the preferred path.  This expression can be a function call, but the called function must be defined in the child `script` element. |
| `search-id` | String | Optional if `type` is `component`; otherwise, not allowed.  The ID of another search. The other search is performed, and its results further filtered by removing those results that don’t match the version strings given by the child `bundle` element. This allows the other search to be qualified for certain values of `CFBundleShortVersionStrings` or `CFBundleVersions`. |
| `search-path` | String | Optional if `type` is `component`; otherwise, not allowed.  A path to a bundle. If there is a bundle at this path that matches the version string of this element’s child `bundle` element, then the path is used as the search result. |
| `type` | String | _Required._ Indicates the type of the search. Valid values are:  `component` Search for a bundle on disk that matches the identifier and version strings given by the child `bundle` element. By default, the Installer uses Launches Services to perform the search, and it searches only the volume that the user selected as the installation target. The `search-id` and `search-path` attributes modify this behavior.  `script` Search by evaluating the JavaScript code contained in the `script` attribute. |

This element must contain exactly one of the following elements:

- [bundle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvztgy): The bundle for a component search.
- [script](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvzrgq): The script for a script search.

_Reserved._

_Reserved._

_Reserved._

Defines the title of the product.

None.

The title or a localization key used to look up the title.

Specifies whether a particular volume meets the distribution’s volume requirements. All of the tests in the `script` attribute and the child elements must pass.

| Attribute name | Type | Description |
| --- | --- | --- |
| `script` | Boolean JavaScript expression | _Required._ Specifies whether the requirements for installing on a particular volume are met.  If the script evaluates to `false`, it must also set `my.result.type` and `my.result.message` to indicate the severity of the problem and provide a message to display.  The property `my.target.mountpoint` contains the mount point of the volume being checked. |

This element can contain the following elements:

- [allowed-os-versions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvztgm) (zero or one): The versions of the OS to accept on the target volume.
- [required-bundles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnzqfvbuqmjqgawvgvztha) (zero or one): The bundles that must already be present.

Specifies text that is displayed by Installer at the beginning of the installation process.

| Attribute name | Type | Description |
| --- | --- | --- |
| `file` | String | _Required._ The filename of the welcome file in the distribution package—for example, `welcome.rtf`. |
| `mime-type` | String | The MIME-type specifier for the data contained in the file. |
| `uti` | String | The UTI-type specifier for the data contained in the file. |
| `language` | - | _Reserved._ |

None.

[Next](Document%20Revision%20History.md)[Previous](About%20Distribution%20Definition%20Files.md)

