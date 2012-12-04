# Sublime Text 2 plugin: Textmaster Framework



## Shortcut Keys

**OSX:**

`CTRL+J` - Create JS Framework files

Type `client_area/index` and which creates `app/assets/javascripts/src/pages/client_area/index` with two files:

`controller.coffee`

```coffeescript
#= require './view'
module = Textmaster.ClientArea.Index

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

### Git
Sublime Text 2 stores nearly all of the interesting files for users under the data directory. This is a platform-dependent location:

 * Windows: %APPDATA%\Sublime Text 2\Packages
 * OS X: ~/Library/Application Support/Sublime Text 2/Packages
 * Linux: ~/.Sublime Text 2/Packages

This method required a little more work, but simply clone this repo into your Sublime Text 2 Package directory.

    $ git clone git@github.com:apneadiving/TextmasterSublimePlugin.git

