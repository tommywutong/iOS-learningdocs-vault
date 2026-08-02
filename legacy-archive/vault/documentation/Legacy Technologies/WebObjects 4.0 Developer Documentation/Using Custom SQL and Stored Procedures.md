---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/FetchSpecs7.html
archived_at: '2026-07-18T01:18:32.855519Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Fetch%20Specifications.md) [!Previous Section](Configuring%20Raw%20Row%20Fetching.md)

# Using Custom SQL and Stored Procedures

Instead of building a qualifier for the fetch specification to fetch with, you can specify custom SQL or a stored procedure. To do so, use the SQL tab of the Fetch Specification Builder, as shown in [Figure 47](#apple-ge3dkmjq).

!

Figure 47. Using a Custom SQL Expression or a Stored Procedure

To use custom SQL, check the "Use Raw SQL Expression" box, and provide the SQL in the text field just below the box. If you've built a qualifier in the Qualifier Builder, this text field is initialized with the corresponding SQL. Checking the "Use Raw SQL Expression" box enables this text field so you can modify the text. Note that the Fetch Specification Builder isn't able to parse arbitrary SQL to produce a corresponding qualifier in the Qualifier Builder.
To use a stored procedure, check the "Use Stored Procedures" box, and choose the stored procedure from the list just below the box. The stored procedure must be defined in the model.

[!Table of Contents](Fetch%20Specifications.md) [!Next Section](Testing%20a%20Fetch%20Specification.md)
