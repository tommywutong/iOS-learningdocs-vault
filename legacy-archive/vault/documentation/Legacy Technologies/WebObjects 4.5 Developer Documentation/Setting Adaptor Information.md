---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/EOTools/Database1.html
archived_at: '2026-07-15T08:03:47.700356Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Tools and Techniques

[!Table of Contents](Interacting%20with%20a%20Database.md) [!Previous Section](Interacting%20with%20a%20Database.md)

# Setting Adaptor Information

A model includes a connection dictionary, which contains the information needed to connect to a database server. The keys of the connection dictionary identify the information the server expects, and the values associated with those keys are the values that the adaptor tries when logging into the database.
When you initialize an adaptor from a model, any connection information stored with the model is copied into the adaptor object.
The connection dictionary contains the last values you entered in the login panel and saved as a part of your model (so long as you haven't manually edited the connection dictionary in your model file). You can change the connection dictionary's values from EOModeler; this is called setting adaptor information.
To set adaptor information:

- Choose Model ! Set Adaptor Info.

EOModeler displays a login panel that contains values taken from the model's connection dictionary.

- In the login panel, make the edits you want reflected in your connection dictionary, and click OK.

For example, if you specified a user name and password to log into a database and create your model, you can remove that information from the connection dictionary by clearing those fields in the login panel. Then, in your application, you can prompt the user for a user name and password by sending a __runLoginPanelAndValidateConnectionDictionary__ message to your adaptor object.
You can also edit the connection dictionary in its raw form using the Connection Dictionary Inspector. This provides you access to connection dictionary entries that the login panel doesn't configure. To use the Connection Dictionary Inspector, select the model icon in the Model Editor, and display the Inspector.

!

Figure 48. Connection Dictionary Inspector

For more discussion of how Enterprise Objects Framework manages database connections and connection dictionaries, see the chapter "Connecting to the Database" in the book _Enterprise Objects Framework Developer's Guide_.

## Switching Adaptors

You can change the database and adaptor your model is based on. To do so:

- Choose Model ! Switch Adaptor.

This displays a New Model panel listing all the available adaptors.

- Select the adaptor you want to switch to and click OK.

EOModeler displays the login panel for the database that corresponds to the adaptor you selected.

- Fill in the login panel and click OK.

When you switch adaptors, Enterprise Objects Framework automatically updates the mapping between the internal and external (database) types to work with the new adaptor's database.

[!Table of Contents](Interacting%20with%20a%20Database.md) [!Next Section](Using%20the%20Data%20Browser.md)
