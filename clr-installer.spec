#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-installer
Version  : 2.3.7
Release  : 48
URL      : https://github.com/clearlinux/clr-installer/archive/2.3.7.tar.gz
Source0  : https://github.com/clearlinux/clr-installer/archive/2.3.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0-only
Requires: clr-installer-bin = %{version}-%{release}
Requires: clr-installer-data = %{version}-%{release}
Requires: clr-installer-services = %{version}-%{release}
BuildRequires : buildreq-golang
BuildRequires : glib-dev
BuildRequires : gtk3-dev
Patch1: 0001-Allow-for-equals-characters-in-config-URLs.patch

%description
# Clear Linux Installer
## Clear Linux OS Security
As the installer is a part of the Clear Linux OS distribution, this program follows the [Clear Linux OS Security processes](https://clearlinux.org/documentation/clear-linux/concepts/security).

%package bin
Summary: bin components for the clr-installer package.
Group: Binaries
Requires: clr-installer-data = %{version}-%{release}
Requires: clr-installer-services = %{version}-%{release}

%description bin
bin components for the clr-installer package.


%package data
Summary: data components for the clr-installer package.
Group: Data

%description data
data components for the clr-installer package.


%package extras
Summary: extras components for the clr-installer package.
Group: Default

%description extras
extras components for the clr-installer package.


%package services
Summary: services components for the clr-installer package.
Group: Systemd services

%description services
services components for the clr-installer package.


%prep
%setup -q -n clr-installer-2.3.7
cd %{_builddir}/clr-installer-2.3.7
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1578284783
export GCC_IGNORE_WERROR=1
export GOPROXY=file:///usr/share/goproxy
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1578284783
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-installer

%files data
%defattr(-,root,root,-)
/usr/share/clr-installer/iso_templates/initrd_init_template
/usr/share/clr-installer/iso_templates/isolinux.cfg.template
/usr/share/clr-installer/themes/clr-installer.theme
/usr/share/clr-installer/themes/style.css
/usr/share/defaults/clr-installer/bundles.json
/usr/share/defaults/clr-installer/chpasswd
/usr/share/defaults/clr-installer/clr-installer.yaml
/usr/share/defaults/clr-installer/kernels.json
/usr/share/locale/en_US/LC_MESSAGES/clr-installer.po
/usr/share/locale/es_MX/LC_MESSAGES/clr-installer.po
/usr/share/locale/zh_CN/LC_MESSAGES/clr-installer.po

%files extras
%defattr(-,root,root,-)
/usr/bin/clr-installer-gui
/usr/share/applications/clr-installer-gui.desktop
/usr/share/clr-installer/themes/clr.png
/usr/share/polkit-1/actions/org.clearlinux.clr-installer-gui.policy
/usr/share/polkit-1/rules.d/org.clearlinux.clr-installer-gui.rules

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/clr-installer-provision.service
