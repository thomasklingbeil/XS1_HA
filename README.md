# XS1_HA
EZcontrol® XS1 component for Home Assistant

# Work in progress
This component is in its baby shoes and in no way meant to be used in production.

# Configuration

Just add these two lines to your configuration:

    # XS1 Gateway
    xs1:
      host: "192.168.2.75"
      
The component will connect to the gateway and pick up all device configurations automatically.
If you change the configuration for a device on the XS1 gateway you currently have to restart home assistant to trigger an update.

# License
    XS1_HA by Markus Ressel
    Copyright (C) 2017  Markus Ressel

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
