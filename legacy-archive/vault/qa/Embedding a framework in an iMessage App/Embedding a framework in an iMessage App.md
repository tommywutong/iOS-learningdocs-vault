---
title: Embedding a framework in an iMessage App
apple_id: DTS40017538
resource_type: QA
platform: iOS
topic: null
technology: MessageUI
published: '2017-09-26'
source_url: https://developer.apple.com/library/archive/qa/qa1936/_index.html
archived_at: '2026-07-18T02:37:14.876634Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1936

# Embedding a framework in an iMessage App

## Q:  How do I embed a framework in an iMessage App?

A: Xcode 8.0 does not expose the ability to embed a framework in the stub application target containing your iMessage App. If you need to use a framework in an iMessage App, you can use an alternate approach.

There are two approaches to consider. The first approach is to compile the code from the framework directly into the iMessage Extension. The second approach uses an aggregate target with a Run Script build phase to move the framework to the correct location in the app bundle. The remainder of this document focuses on the second approach, which requires familiarity with configuring targets and build settings in Xcode.

The framework target must be a dependency of the aggregate target. The aggregate target must be a dependency of the iMessage Extension target. Configured targets are shown in Figure 1 and Figure 2.

__Figure 1__  The aggregate target depends on the framework target

!!

__Figure 2__  The iMessage Extension depends on the aggregate target

!!

The correct location for the framework is different for archive builds and development builds:

- Archive build: `${DSTROOT}/Applications/MyMessageApp.app/Frameworks`
- Development build: `${BUILT_PRODUCTS_DIR}/MyMessageApp.app/Frameworks`

The [DEPLOYMENT_LOCATION](https://developer.apple.com/library/ios/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW37) build setting determines which location to use. When `DEPLOYMENT_LOCATION` is `YES`, the build is for an archive, and when set to `NO`, the build is for development.

Configure the aggregate target with a Run Script build phase that copies the framework to the proper location, as shown in Listing 1. You must modify this script to replace `MyMessageApp.app` with the name of your iMessage app bundle, and to replace `MyFramework.framework` with the name of your framework.

__Listing 1__  Shell script to move the framework to the app bundle

```
if [ "${DEPLOYMENT_LOCATION}" = "YES" ] ; then
    FRAMEWORKS_DIR="${DSTROOT}/Applications/MyMessageApp.app/Frameworks"
else
    FRAMEWORKS_DIR="${BUILT_PRODUCTS_DIR}/MyMessageApp.app/Frameworks"
fi

rm -rf "${FRAMEWORKS_DIR}/MyFramework.framework"
mkdir -p "${FRAMEWORKS_DIR}"
cp -r "${BUILT_PRODUCTS_DIR}/MyFramework.framework" "${FRAMEWORKS_DIR}"
```


In order to run an iMessage App on a device, the framework must be code signed with the same signing identity used to sign the iMessage App.

If you are building the framework, you can do this by configuring the framework target to be code signed during its build. Figure 3 shows the build settings for this.

If you are not building the framework, or if configuring the framework to be signed during building is not an option, the shell script in [Copying the Framework Into the App](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjthawugsbrfvbu6uczjfheo) needs to call the codesign tool to sign the framework with the correct signing identity after copying the framework to the app.

__Figure 3__  Code signing settings for the framework

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-09-26 | Marked document as Legacy. Added a link to the replacement Embedding Frameworks In An App tech note. |
| 2017-03-21 | Marked document as Legacy. Added a link to the replacement Embedding Frameworks In An App tech note. |
|  | Marked document as Legacy. Added a link to the replacement Embedding Frameworks In An App tech note. |
| 2016-09-02 | New document that demonstrates how to embed a framework in an iMessage App |

