---
title: iSight - Configuring gain settings for IIDC cameras
apple_id: DTS10003535
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2005-04-06'
source_url: https://developer.apple.com/library/archive/qa/qa1421/_index.html
archived_at: '2026-07-18T02:30:38.667788Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1421

# iSight - Configuring gain settings for IIDC cameras

## Q:  My application captures video from the iSight camera but in order to process the frames I need to make sure the gain adjustment is turned on and set to a certain value at specific times. What's the best way to do this?

A: `SGSettingsDialog` lets you configure a number of IIDC camera specific features via the Adjustments panel, and any IIDC feature you can configure with the Adjustments panel can also be configured using the VDIIDC APIs. Therefore, this gives developers a couple of options:

The most straight forward approach is to use [SGSettingsDialog](https://developer.apple.com/documentation/QuickTime/APIREF/sgsettingsdialog.htm) to configure the Video Channel, then save and load those settings as required using [SGGetChannelSettings](https://developer.apple.com/documentation/QuickTime/APIREF/sggetchannelsettings.htm) and [SGSetChannelSettings](https://developer.apple.com/documentation/QuickTime/APIREF/sgsetchannelsettings.htm) as discussed in [Q&A1286](https://developer.apple.com/qa/qa2001/qa1286.html).

Alternatively, you can use the VDIIDC APIs directly and while slightly more complex, they may be more appropriate depending on the situation.

Different IIDC cameras can support a number of different features. This feature information can be retrieved using one of the VDIIDCGetFeatures APIs and is returned in a hierarchy of QuickTime Atoms as shown in Figure 1. The Atom Container can then be parsed into the appropriate settings structures.

__Figure 1__  IIDC Atom Hierarchy.

!

A full description of Atom types and VDIIDC APIs can be found in the [New IIDC Digitizer Functions](https://developer.apple.com/documentation/QuickTime/WhatsNewQT6_4/Chap1/chapter_1_section_14.html#//apple_ref/doc/uid/TP30000902-CH240-BBCDAECB) section of [What's new in QuickTime 6.4](https://developer.apple.com/documentation/QuickTime/WhatsNewQT6_4/Chap1/chapter_1_section_1.html).

__Listing 1__  Configuring Gain using VDIIDC APIs.

```
ComponentResult ConfigureGain(SGChannel inChannel)
{
    QTAtomContainer         atomContainer;
    QTAtom                  featureAtom;
    VDIIDCFeatureSettings   settings;
    VideoDigitizerComponent vd;
    ComponentDescription    desc;
    ComponentResult         result = paramErr;

    if (NULL == inChannel) goto bail;

    // get the digitizer and make sure it's legit
    vd = SGGetVideoDigitizerComponent(inChannel);
    if (NULL == vd) goto bail;

    GetComponentInfo((Component)vd, &desc, NULL, NULL, NULL);
    if (vdSubtypeIIDC != desc.componentSubType) goto bail;

    // *** now do the real work ***

    // return the gain feature in an atom container
    result = VDIIDCGetFeaturesForSpecifier(vd, vdIIDCFeatureGain, &atomContainer);
    if (noErr == result) {

        // find the feature atom
        featureAtom = QTFindChildByIndex(atomContainer, kParentAtomIsContainer,
                                         vdIIDCAtomTypeFeature, 1, NULL);
        if (0 == featureAtom) { result = cannotFindAtomErr; goto bail; }

        // find the gain settings from the feature atom and copy the data
        // into our settings
        result = QTCopyAtomDataToPtr(atomContainer,
                                     QTFindChildByID(atomContainer, featureAtom,
                                     vdIIDCAtomTypeFeatureSettings,
                                     vdIIDCAtomIDFeatureSettings, NULL),
                                     true, sizeof(settings), &settings, NULL);
        if (noErr == result) {
            /* When indicating capabilities, the flag being set indicates that the
               feature can be put into the given state.
               When indicating/setting state, the flag represents the current/desired
               state. Note that certain combinations of flags are valid for capabilities
               (i.e. vdIIDCFeatureFlagOn | vdIIDCFeatureFlagOff) but are mutually
               exclusive for state.
             */
            // is the setting supported?
            if (settings.capabilities.flags & (vdIIDCFeatureFlagOn |
                                               vdIIDCFeatureFlagManual |
                                               vdIIDCFeatureFlagRawControl)) {
                // set state flags
                settings.state.flags = (vdIIDCFeatureFlagOn |
                                        vdIIDCFeatureFlagManual |
                                        vdIIDCFeatureFlagRawControl);

                // set value - will either be 500 or the max value supported by
                // the camera represented in a float between 0 and 1.0
                settings.state.value = (1.0 / settings.capabilities.rawMaximum) *
                                       ((settings.capabilities.rawMaximum > 500) ? 500 :
                                       settings.capabilities.rawMaximum);

                // store the result back in the container
                result = QTSetAtomData(atomContainer,
                                       QTFindChildByID(atomContainer, featureAtom,
                                       vdIIDCAtomTypeFeatureSettings,
                                       vdIIDCAtomIDFeatureSettings, NULL),
                                       sizeof(settings), &settings);
                if (noErr == result) {
                    // set it on the device
                    result = VDIIDCSetFeatures(vd, atomContainer);
                }
            } else {
                // can't do it!
                result = featureUnsupported;
            }
        }
    }

bail:
    return result;
}
```

Different camera models may also behave differently when specific settings are changed and certain cameras may not have certain features available.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-04-06 | New document that discusses how to configure features of IIDC cameras, specifically gain for the iSight |

