---
title: Locale.Region
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/region-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/locale/region-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/region-swift.struct.json'
content_hash: 'sha256:5f30601295a9afd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# Locale.Region

<sub>Structure</sub>

A type that represents a geographic region, for use in specifying a locale or language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Region
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringLiteral](../../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../../swift/expressiblebyunicodescalarliteral.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a region

- [init(_:)](<region-swift.struct/init(__).md>) — Creates a region from a BCP 47 identifier.
- [init(stringLiteral:)](<region-swift.struct/init(stringliteral_).md>) — Creates a region from a BCP 47 identifier as a string literal.

### Examining region properties

- [identifier](region-swift.struct/identifier.md) — The BCP 47 identifier of the region.
- [containingRegion](region-swift.struct/containingregion.md) — The region that contains this region, if any.
- [continent](region-swift.struct/continent.md) — The continent that contains this region, if any.
- [isISORegion](region-swift.struct/isisoregion.md) — A Boolean value that indicates whether the region is an ISO-defined region.
- [subRegions](region-swift.struct/subregions.md) — An array of all the sub-regions of the region.

### Using special-purpose regions

- [unknown](region-swift.struct/unknown.md) — A pre-defined unknown or invalid region.

### Getting a list of regions

- [isoRegions](region-swift.struct/isoregions.md) — An array of regions defined by ISO.

### Structures

- [Category](region-swift.struct/category-swift.struct.md) — Categories of a region. See https://www.unicode.org/reports/tr35/tr35-35/tr35-info.html#Territory_Data

### Instance Properties

- [category](region-swift.struct/category-swift.property.md) — The category of the region.
- [subcontinent](region-swift.struct/subcontinent.md) — The subcontinent that contains this region, if any.

### Instance Methods

- [subRegions(ofCategory:)](<region-swift.struct/subregions(ofcategory_).md>) — An array of the sub-regions, matching the specified category of the region.

### Type Properties

- [ålandIslands](region-swift.struct/_landislands.md)
- [afghanistan](region-swift.struct/afghanistan.md)
- [albania](region-swift.struct/albania.md)
- [algeria](region-swift.struct/algeria.md)
- [americanSamoa](region-swift.struct/americansamoa.md)
- [andorra](region-swift.struct/andorra.md)
- [angola](region-swift.struct/angola.md)
- [anguilla](region-swift.struct/anguilla.md)
- [antarctica](region-swift.struct/antarctica.md)
- [antiguaBarbuda](region-swift.struct/antiguabarbuda.md)
- [argentina](region-swift.struct/argentina.md)
- [armenia](region-swift.struct/armenia.md)
- [aruba](region-swift.struct/aruba.md)
- [ascensionIsland](region-swift.struct/ascensionisland.md)
- [australia](region-swift.struct/australia.md)
- [austria](region-swift.struct/austria.md)
- [azerbaijan](region-swift.struct/azerbaijan.md)
- [bahamas](region-swift.struct/bahamas.md)
- [bahrain](region-swift.struct/bahrain.md)
- [bangladesh](region-swift.struct/bangladesh.md)
- [barbados](region-swift.struct/barbados.md)
- [belarus](region-swift.struct/belarus.md)
- [belgium](region-swift.struct/belgium.md)
- [belize](region-swift.struct/belize.md)
- [benin](region-swift.struct/benin.md)
- [bermuda](region-swift.struct/bermuda.md)
- [bhutan](region-swift.struct/bhutan.md)
- [bolivia](region-swift.struct/bolivia.md)
- [bosniaHerzegovina](region-swift.struct/bosniaherzegovina.md)
- [botswana](region-swift.struct/botswana.md)
- [bouvetIsland](region-swift.struct/bouvetisland.md)
- [brazil](region-swift.struct/brazil.md)
- [britishVirginIslands](region-swift.struct/britishvirginislands.md)
- [brunei](region-swift.struct/brunei.md)
- [bulgaria](region-swift.struct/bulgaria.md)
- [burkinaFaso](region-swift.struct/burkinafaso.md)
- [burundi](region-swift.struct/burundi.md)
- [côteDIvoire](region-swift.struct/c_tedivoire.md)
- [cambodia](region-swift.struct/cambodia.md)
- [cameroon](region-swift.struct/cameroon.md)
- [canada](region-swift.struct/canada.md)
- [canaryIslands](region-swift.struct/canaryislands.md)
- [capeVerde](region-swift.struct/capeverde.md)
- [caribbeanNetherlands](region-swift.struct/caribbeannetherlands.md)
- [caymanIslands](region-swift.struct/caymanislands.md)
- [centralAfricanRepublic](region-swift.struct/centralafricanrepublic.md)
- [ceutaMelilla](region-swift.struct/ceutamelilla.md)
- [chad](region-swift.struct/chad.md)
- [chagosArchipelago](region-swift.struct/chagosarchipelago.md)
- [chile](region-swift.struct/chile.md)
- [chinaMainland](region-swift.struct/chinamainland.md)
- [christmasIsland](region-swift.struct/christmasisland.md)
- [clippertonIsland](region-swift.struct/clippertonisland.md)
- [cocosIslands](region-swift.struct/cocosislands.md)
- [colombia](region-swift.struct/colombia.md)
- [comoros](region-swift.struct/comoros.md)
- [congoBrazzaville](region-swift.struct/congobrazzaville.md)
- [congoKinshasa](region-swift.struct/congokinshasa.md)
- [cookIslands](region-swift.struct/cookislands.md)
- [costaRica](region-swift.struct/costarica.md)
- [croatia](region-swift.struct/croatia.md)
- [cuba](region-swift.struct/cuba.md)
- [curaçao](region-swift.struct/cura_ao.md)
- [cyprus](region-swift.struct/cyprus.md)
- [czechia](region-swift.struct/czechia.md)
- [denmark](region-swift.struct/denmark.md)
- [diegoGarcia](region-swift.struct/diegogarcia.md)
- [djibouti](region-swift.struct/djibouti.md)
- [dominica](region-swift.struct/dominica.md)
- [dominicanRepublic](region-swift.struct/dominicanrepublic.md)
- [ecuador](region-swift.struct/ecuador.md)
- [egypt](region-swift.struct/egypt.md)
- [elSalvador](region-swift.struct/elsalvador.md)
- [equatorialGuinea](region-swift.struct/equatorialguinea.md)
- [eritrea](region-swift.struct/eritrea.md)
- [estonia](region-swift.struct/estonia.md)
- [eswatini](region-swift.struct/eswatini.md)
- [ethiopia](region-swift.struct/ethiopia.md)
- [falklandIslands](region-swift.struct/falklandislands.md)
- [faroeIslands](region-swift.struct/faroeislands.md)
- [fiji](region-swift.struct/fiji.md)
- [finland](region-swift.struct/finland.md)
- [france](region-swift.struct/france.md)
- [frenchGuiana](region-swift.struct/frenchguiana.md)
- [frenchPolynesia](region-swift.struct/frenchpolynesia.md)
- [frenchSouthernTerritories](region-swift.struct/frenchsouthernterritories.md)
- [gabon](region-swift.struct/gabon.md)
- [gambia](region-swift.struct/gambia.md)
- [georgia](region-swift.struct/georgia.md)
- [germany](region-swift.struct/germany.md)
- [ghana](region-swift.struct/ghana.md)
- [gibraltar](region-swift.struct/gibraltar.md)
- [greece](region-swift.struct/greece.md)
- [greenland](region-swift.struct/greenland.md)
- [grenada](region-swift.struct/grenada.md)
- [guadeloupe](region-swift.struct/guadeloupe.md)
- [guam](region-swift.struct/guam.md)
- [guatemala](region-swift.struct/guatemala.md)
- [guernsey](region-swift.struct/guernsey.md)
- [guinea](region-swift.struct/guinea.md)
- [guineaBissau](region-swift.struct/guineabissau.md)
- [guyana](region-swift.struct/guyana.md)
- [haiti](region-swift.struct/haiti.md)
- [heardMcdonaldIslands](region-swift.struct/heardmcdonaldislands.md)
- [honduras](region-swift.struct/honduras.md)
- [hongKong](region-swift.struct/hongkong.md)
- [hungary](region-swift.struct/hungary.md)
- [iceland](region-swift.struct/iceland.md)
- [india](region-swift.struct/india.md)
- [indonesia](region-swift.struct/indonesia.md)
- [iran](region-swift.struct/iran.md)
- [iraq](region-swift.struct/iraq.md)
- [ireland](region-swift.struct/ireland.md)
- [isleOfMan](region-swift.struct/isleofman.md)
- [israel](region-swift.struct/israel.md)
- [italy](region-swift.struct/italy.md)
- [jamaica](region-swift.struct/jamaica.md)
- [japan](region-swift.struct/japan.md)
- [jersey](region-swift.struct/jersey.md)
- [jordan](region-swift.struct/jordan.md)
- [kazakhstan](region-swift.struct/kazakhstan.md)
- [kenya](region-swift.struct/kenya.md)
- [kiribati](region-swift.struct/kiribati.md)
- [kosovo](region-swift.struct/kosovo.md)
- [kuwait](region-swift.struct/kuwait.md)
- [kyrgyzstan](region-swift.struct/kyrgyzstan.md)
- [laos](region-swift.struct/laos.md)
- [latinAmerica](region-swift.struct/latinamerica.md)
- [latvia](region-swift.struct/latvia.md)
- [lebanon](region-swift.struct/lebanon.md)
- [lesotho](region-swift.struct/lesotho.md)
- [liberia](region-swift.struct/liberia.md)
- [libya](region-swift.struct/libya.md)
- [liechtenstein](region-swift.struct/liechtenstein.md)
- [lithuania](region-swift.struct/lithuania.md)
- [luxembourg](region-swift.struct/luxembourg.md)
- [macao](region-swift.struct/macao.md)
- [madagascar](region-swift.struct/madagascar.md)
- [malawi](region-swift.struct/malawi.md)
- [malaysia](region-swift.struct/malaysia.md)
- [maldives](region-swift.struct/maldives.md)
- [mali](region-swift.struct/mali.md)
- [malta](region-swift.struct/malta.md)
- [marshallIslands](region-swift.struct/marshallislands.md)
- [martinique](region-swift.struct/martinique.md)
- [mauritania](region-swift.struct/mauritania.md)
- [mauritius](region-swift.struct/mauritius.md)
- [mayotte](region-swift.struct/mayotte.md)
- [mexico](region-swift.struct/mexico.md)
- [micronesia](region-swift.struct/micronesia.md)
- [moldova](region-swift.struct/moldova.md)
- [monaco](region-swift.struct/monaco.md)
- [mongolia](region-swift.struct/mongolia.md)
- [montenegro](region-swift.struct/montenegro.md)
- [montserrat](region-swift.struct/montserrat.md)
- [morocco](region-swift.struct/morocco.md)
- [mozambique](region-swift.struct/mozambique.md)
- [myanmar](region-swift.struct/myanmar.md)
- [namibia](region-swift.struct/namibia.md)
- [nauru](region-swift.struct/nauru.md)
- [nepal](region-swift.struct/nepal.md)
- [netherlands](region-swift.struct/netherlands.md)
- [newCaledonia](region-swift.struct/newcaledonia.md)
- [newZealand](region-swift.struct/newzealand.md)
- [nicaragua](region-swift.struct/nicaragua.md)
- [niger](region-swift.struct/niger.md)
- [nigeria](region-swift.struct/nigeria.md)
- [niue](region-swift.struct/niue.md)
- [norfolkIsland](region-swift.struct/norfolkisland.md)
- [northMacedonia](region-swift.struct/northmacedonia.md)
- [northernMarianaIslands](region-swift.struct/northernmarianaislands.md)
- [norway](region-swift.struct/norway.md)
- [oman](region-swift.struct/oman.md)
- [pakistan](region-swift.struct/pakistan.md)
- [palau](region-swift.struct/palau.md)
- [palestinianTerritories](region-swift.struct/palestinianterritories.md)
- [panama](region-swift.struct/panama.md)
- [papuaNewGuinea](region-swift.struct/papuanewguinea.md)
- [paraguay](region-swift.struct/paraguay.md)
- [peru](region-swift.struct/peru.md)
- [philippines](region-swift.struct/philippines.md)
- [pitcairnIslands](region-swift.struct/pitcairnislands.md)
- [poland](region-swift.struct/poland.md)
- [portugal](region-swift.struct/portugal.md)
- [puertoRico](region-swift.struct/puertorico.md)
- [qatar](region-swift.struct/qatar.md)
- [réunion](region-swift.struct/r_union.md)
- [romania](region-swift.struct/romania.md)
- [russia](region-swift.struct/russia.md)
- [rwanda](region-swift.struct/rwanda.md)
- [sãoToméPríncipe](region-swift.struct/s_otom_pr_ncipe.md)
- [saintBarthélemy](region-swift.struct/saintbarth_lemy.md)
- [saintHelena](region-swift.struct/sainthelena.md)
- [saintKittsNevis](region-swift.struct/saintkittsnevis.md)
- [saintLucia](region-swift.struct/saintlucia.md)
- [saintMartin](region-swift.struct/saintmartin.md)
- [saintPierreMiquelon](region-swift.struct/saintpierremiquelon.md)
- [saintVincentGrenadines](region-swift.struct/saintvincentgrenadines.md)
- [samoa](region-swift.struct/samoa.md)
- [sanMarino](region-swift.struct/sanmarino.md)
- [saudiArabia](region-swift.struct/saudiarabia.md)
- [senegal](region-swift.struct/senegal.md)
- [serbia](region-swift.struct/serbia.md)
- [seychelles](region-swift.struct/seychelles.md)
- [sierraLeone](region-swift.struct/sierraleone.md)
- [singapore](region-swift.struct/singapore.md)
- [sintMaarten](region-swift.struct/sintmaarten.md)
- [slovakia](region-swift.struct/slovakia.md)
- [slovenia](region-swift.struct/slovenia.md)
- [solomonIslands](region-swift.struct/solomonislands.md)
- [somalia](region-swift.struct/somalia.md)
- [southAfrica](region-swift.struct/southafrica.md)
- [southGeorgiaSouthSandwichIslands](region-swift.struct/southgeorgiasouthsandwichislands.md)
- [southKorea](region-swift.struct/southkorea.md)
- [southSudan](region-swift.struct/southsudan.md)
- [spain](region-swift.struct/spain.md)
- [sriLanka](region-swift.struct/srilanka.md)
- [suriname](region-swift.struct/suriname.md)
- [svalbardJanMayen](region-swift.struct/svalbardjanmayen.md)
- [sweden](region-swift.struct/sweden.md)
- [switzerland](region-swift.struct/switzerland.md)
- [taiwan](region-swift.struct/taiwan.md)
- [tajikistan](region-swift.struct/tajikistan.md)
- [tanzania](region-swift.struct/tanzania.md)
- [thailand](region-swift.struct/thailand.md)
- [timorLeste](region-swift.struct/timorleste.md)
- [togo](region-swift.struct/togo.md)
- [tokelau](region-swift.struct/tokelau.md)
- [tonga](region-swift.struct/tonga.md)
- [trinidadTobago](region-swift.struct/trinidadtobago.md)
- [tristanDaCunha](region-swift.struct/tristandacunha.md)
- [tunisia](region-swift.struct/tunisia.md)
- [turkey](region-swift.struct/turkey.md)
- [turkmenistan](region-swift.struct/turkmenistan.md)
- [turksCaicosIslands](region-swift.struct/turkscaicosislands.md)
- [tuvalu](region-swift.struct/tuvalu.md)
- [uganda](region-swift.struct/uganda.md)
- [ukraine](region-swift.struct/ukraine.md)
- [unitedArabEmirates](region-swift.struct/unitedarabemirates.md)
- [unitedKingdom](region-swift.struct/unitedkingdom.md)
- [unitedStates](region-swift.struct/unitedstates.md)
- [unitedStatesOutlyingIslands](region-swift.struct/unitedstatesoutlyingislands.md)
- [unitedStatesVirginIslands](region-swift.struct/unitedstatesvirginislands.md)
- [uruguay](region-swift.struct/uruguay.md)
- [uzbekistan](region-swift.struct/uzbekistan.md)
- [vanuatu](region-swift.struct/vanuatu.md)
- [vaticanCity](region-swift.struct/vaticancity.md)
- [venezuela](region-swift.struct/venezuela.md)
- [vietnam](region-swift.struct/vietnam.md)
- [wallisFutuna](region-swift.struct/wallisfutuna.md)
- [westernSahara](region-swift.struct/westernsahara.md)
- [world](region-swift.struct/world.md)
- [yemen](region-swift.struct/yemen.md)
- [zambia](region-swift.struct/zambia.md)
- [zimbabwe](region-swift.struct/zimbabwe.md)

### Type Methods

- [isoRegions(ofCategory:)](<region-swift.struct/isoregions(ofcategory_).md>) — An array of regions matching the specified categories.

## See Also

### Getting region components

- [region](region-swift.property.md) — The region used by the locale.
- [subdivision](subdivision-swift.property.md) — The optional subdivision of the region used by this locale.
- [Subdivision](subdivision-swift.struct.md) — A type that represents a subdivision of a region, such as a state in the US or a province in Canada.
- [variant](variant-swift.property.md) — An optional variant used by the locale.
- [Variant](variant-swift.struct.md) — A type that represents a locale’s language variant.
