%global commit 1b6674fe31f7e2f485f4a78f9f3dd53b9753c9d0
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           virtual-playing-orchestra-ardour-template
Version:        2.0.0
Release:        0.20200201.git.%{?shortcommit}%{?dist}
Summary:        Ardour template for orchestral music

# Creative Commons Attribution-ShareAlike 4.0 International Public License
License:        CC-BY-SA
URL:            https://github.com/michaelwillis/virtual-playing-orchestra-ardour-template
Source0:        https://github.com/michaelwillis/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       virtual-playing-orchestra-performance-scripts
Requires:       lv2-sfizz-plugins
Requires:       lv2-dragonfly-reverb-plugins

%global common_description \
An Ardour project template for composing orchestral music on Linux.

%description
%common_description

%package -n virtual-playing-orchestra-ardour5-template
Summary:        Ardour 5 template for orchestral music
Requires:       %{name} = %{version}-%{release}
Requires:       ardour5

%description -n virtual-playing-orchestra-ardour5-template
%common_description

This package contains the Ardour 5 template.

%package -n virtual-playing-orchestra-ardour6-template
Summary:        Ardour 6 template for orchestral music
Requires:       %{name} = %{version}-%{release}
Requires:       ardour6

%description -n virtual-playing-orchestra-ardour6-template
%common_description

This package contains the Ardour 6 template.

%prep
%autosetup -n %{name}-%{commit}

%build
find "Virtual Playing Orchestra/" -name "*.ttl" | while read f; do
	sed -i 's|/opt/Virtual-Playing-Orchestra3|%{_datadir}/soundfonts/virtual-playing-orchestra|' "$f"
done

%install
rm -rf $RPM_BUILD_ROOT

install -d %{buildroot}%{_datadir}/ardour5/templates
install -d %{buildroot}%{_datadir}/ardour6/templates

cp -r "Virtual Playing Orchestra" %{buildroot}%{_datadir}/ardour5/templates/
cp -r "Virtual Playing Orchestra" %{buildroot}%{_datadir}/ardour6/templates/

# https://discourse.ardour.org/t/templates-sometimes-include-absolute-paths-with-my-home-dir/89283 
sed -i 's|/Users/michaelwillis/Library/Preferences/Ardour5|%{_datadir}/ardour5|g' \
 "%{buildroot}%{_datadir}/ardour5/templates/Virtual Playing Orchestra/Virtual Playing Orchestra.template"
sed -i 's|/Users/michaelwillis/Library/Preferences/Ardour5|%{_datadir}/ardour5|g' \
 "%{buildroot}%{_datadir}/ardour6/templates/Virtual Playing Orchestra/Virtual Playing Orchestra.template"

%files
%license license.txt
%doc readme.md seating.png

%files -n virtual-playing-orchestra-ardour5-template
"%{_datadir}/ardour5/templates/Virtual Playing Orchestra"

%files -n virtual-playing-orchestra-ardour6-template
"%{_datadir}/ardour6/templates/Virtual Playing Orchestra"

%changelog
* Fri Apr 17 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.0.0-0.20200201.git.1b6674f
- Initial build
