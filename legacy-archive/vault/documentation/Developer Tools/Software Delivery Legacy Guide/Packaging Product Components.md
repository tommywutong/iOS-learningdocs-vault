---
title: Software Delivery Legacy Guide
apple_id: TP40004615
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2010-09-15'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SoftwareDistribution4/Component_Packages/Component_Packages.html
archived_at: '2026-07-15T07:26:53.392525Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Software Delivery Legacy Guide](Introduction.md)


[Next](Defining%20a%20Managed%20Install.md)[Previous](Managed%20Installs.md)

# Packaging Product Components

After breaking down a product into distinct components (such as applications, frameworks, fonts, documentation, and so on), you create an installation package for each of the product’s components. An _installation package_ is a file package that contains one component and information about the package and its payload. See [What Is a Package?](Managed%20Installs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqnrnknlts) for more information about packages.

The Installer application can open a package and place its payload on a user’s system. Installation packages whose payload is a component of a multicomponent product are known as _component packages_.

To create a component package, you perform the following tasks:

1. Categorize the component.
2. Create the component package project directory.
3. Add the component files to the project directory.
4. Add executables to the project directory if the component requires them.
5. Create the component package.
6. Test the component package.

The following sections describe these tasks in detail.

There are several types of product components available in Mac OS X. Some examples are application packages (file packages that contain an application’s executable code and resources), frameworks (directories that contain shared executable code and resources), font files, and plug-ins. Categorizing a component helps you determine the appropriate installation destination for it. Table 5-1 shows some component categories and corresponding installation destinations. See _[File System Overview](../../Mac%20OSX/File%20System%20Overview/Introduction%20to%20the%20File%20System%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dk2i)_ for detailed information.

__Table 5-1__  Component types and installation destinations

| Type | Destination |
| Application | `/Applications` |
| Framework | `/Library/Frameworks` |
| Font | `/Library/Fonts` |
| Documentation | `/Library/Documentation` |
| Command-line tool | `/usr/local/bin` |

Table 5-2 shows the categorization of a multicomponent product.

__Table 5-2__  Categorization of the components of a multicomponent product, called Levon

| Component | Component type | Installation destination |
| `Levon.app` | Application | `/Applications` |
| `Levon_User_Guide.pdf` | Documentation | `/Library/Documentation` |
| `SharedServices.framework` | Framework | `/Library/Frameworks` |

The component package project directory stores the component’s files, the package project file, and other installation files. For easy identification, you should include the version number of the component in the name of the project directory. For example, Listing 5-1 shows the names of the project directories for the three components of the Levon product.

__Listing 5-1__  Component-package project directories for a multicomponent product

```
LevonApp-1.0.0/
LevonDoc-1.0/
SharedServicesFwk-1.0/
```


Inside the package project directory, create a directory to hold the component files, as shown in the highlighted lines in Listing 5-2.

__Listing 5-2__  Adding component files to component-package project directories

```
LevonApp-1.0.0/
   component/ ```  ``` 
      Levon.app ```  ``` 
LevonDoc-1.0/
   component/ ```  ``` 
      Levon_User_Guide.pdf ```  ``` 
SharedServicesFwk-1.0/
   component/ ```  ``` 
      SharedServices.framework ```  ``` 
```


If your component requires tailored install operations or needs to specify system and volume requirements, add the `extras` directory to the package project directory containing the appropriate executables. Listing 5-3 highlights the `extras` directories in two package project directories.

__Listing 5-3__  Adding executables to component-package project directories

```
LevonApp-1.0.0/
   component/
      Levon.app
   extras/ ```  ``` 
      InstallationCheck ```  ``` 
      VolumeCheck ```  ``` 
      preflight ```  ``` 
      postupgrade ```  ``` 
LevonDoc-1.0/
   component/
      Levon_User_Guide.pdf
SharedServicesFwk-1.0/
   component/
      SharedServices.framework
   extras/ ```  ``` 
      InstallationCheck ```  ``` 
      VolumeCheck ```  ``` 
      preflight ```  ``` 
      postinstall ```  ``` 
      postupgrade ```  ``` 
```

See [Specifying Install Operations](Specifying%20Install%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjufvjvomi) and [Specifying System and Volume Requirements in Pre-Tiger Systems](Specifying%20System%20and%20Volume%20Requirements%20in%20Pre-Tiger%20Systems.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjtfvjvomi) for details on install operations and executable-based installation requirements.

After you have created the package project directory, you use PackageMaker (`/Developer/Applications/Utilities`) to create the component package project file.

To create a component package in PackageMaker:

1. Create a single package project.
2. Enter the package’s title and description.
3. Identify the directory that contains the component’s files (for example, the `component` directory in the package project directory).
4. Edit the component directory’s ownership and access permissions settings using the File Permissions editor.

   The files that the Installer application places on the installation host have the ownership and access permissions specified in the component files in the package. Therefore, you must set up the owner and access permissions of component files appropriately before generating the installation package; otherwise, users may have difficulty manipulating those files after they are installed. In most cases, the owner should be `root` and the group `admin`. Use the permissions recommended in the File Permissions editor.
5. Set the installation destination for the component, and specify an appropriate authentication level and postinstallation process action, if needed.
6. Identify the subdirectory in the project directory that contains executable files that specify installation requirements or install operations, if needed.
7. Set the package identifier and version number.

   A package’s identifier and version number help the Installer application determine the best way to update a product’s files during an install on a system on which the package has already been installed. You must set these two package properties for every package you create.

   For applications and frameworks, use the bundle identifier (`CFBundleIdentifier`) specified in their `Info.plist` files as a starting point. For example, if the bundle ID of an application is `com.mycompany.Levon`, the package identifier should be `com.mycompany.Levon.pkg`. Keep in mind that the package identifier must be unique. (For detailed information on the `CFBundleIdentifier` and other `Info.plist` keys, see _[Runtime Configuration Guidelines](../../Mac%20OSX/Runtime%20Configuration%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3ta2i)_.)

   The package version for application, framework, and plug-in component packages should be the value for the `CFBundleShortVersionString` property of the component they contain. In framework component packages, use the value for the `CFBundleVersion` property. For other component types, choose an appropriate package identifier and package version number.

After you’ve defined a package, use the PackageMaker Build command to generate the component package (`.pkg`) file. You can also save the package project file in the project directory for future use.

Before adding a component package to a metapackage or a distribution package, it’s good practice to ensure that the package installs correctly on its own. You accomplish this task by opening the package in the Installer application and performing the installation process, confirming that the component files are installed correctly.

[Next](Defining%20a%20Managed%20Install.md)[Previous](Managed%20Installs.md)

