# Sublime Text 2 plugin: Textmaster Framework



## Shortcut Keys

**OSX:**

 * `CTRL+J` - Create JS Framework files
 * `SHIFT+CTRL+J` - Create JS Framework files

Type `client_area/index` and which creates `app/assets/javascripts/src/pages/client_area/index` with two files:

`controller.coffee`

```coffeescript
#= require './view'
module = Textmaster.Client.Area.Index

class module.Controller extends Framework.Controller
 @options {
   View: module.View
     events:
       'event_name': { el: 'elt_name', type: 'click' }
 }
```

`view.coffee`

```coffeescript
module = Textmaster.Client.Area.Index

class module.View extends Framework.View
 @options {
   selectors:
     your_selector:
}
```

## Installation

You have two options, we'll start with the preferred installation method.


### Package Control

The easiest and preferred way to of installing this plugin is with [Package Control](http://wbond.net/sublime\_packages/package\_control).

 * Ensure Package Control is installed and Sublime Text 2 has been restarted.
 * Open the Command Palette (Command+Shift+P on OS X, Control+Shift+P on Linux/Windows).
 * Select "Package Control: Install Package"
 * Select Rails Partial when the list appears.

Package Control will automatically keep Rails Partial up to date with the latest version.


### Git

This method required a little more work, but simply clone this repo into your Sublime Text 2 Package directory.

    $ git clone git://github.com/wesf90/rails-partial.git Rails Partial

Into your Package directory:
