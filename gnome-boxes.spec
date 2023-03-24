#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : gnome-boxes
Version  : 44.0
Release  : 42
URL      : https://download.gnome.org/sources/gnome-boxes/44/gnome-boxes-44.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-boxes/44/gnome-boxes-44.0.tar.xz
Summary  : Library for reading and writing virtual machine images in the Open Virtualization Format
Group    : Development/Tools
License  : CC-BY-2.0 LGPL-2.0 LGPL-2.1
Requires: gnome-boxes-bin = %{version}-%{release}
Requires: gnome-boxes-data = %{version}-%{release}
Requires: gnome-boxes-lib = %{version}-%{release}
Requires: gnome-boxes-libexec = %{version}-%{release}
Requires: gnome-boxes-license = %{version}-%{release}
Requires: gnome-boxes-locales = %{version}-%{release}
Requires: libosinfo
Requires: osinfo-db-tools
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : libarchive-dev
BuildRequires : libgudev-dev
BuildRequires : libhandy-dev
BuildRequires : libsoup-dev
BuildRequires : libusb-dev
BuildRequires : pkgconfig(gtk-vnc-2.0)
BuildRequires : pkgconfig(gtksourceview-4)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libosinfo-1.0)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libsoup-3.0)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(libvirt-gconfig-1.0)
BuildRequires : pkgconfig(tracker-sparql-3.0)
BuildRequires : pkgconfig(vte-2.91)
BuildRequires : pkgconfig(webkit2gtk-4.1)
BuildRequires : pkgconfig(winpr2)
BuildRequires : spice-gtk
BuildRequires : spice-gtk-dev
BuildRequires : vte-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-Clear-Linux-as-recommended-distro.patch

%description
# This is the directory where we put upstream vapi bindings when they
# are outdated and we need a version with additional fixes.

%package bin
Summary: bin components for the gnome-boxes package.
Group: Binaries
Requires: gnome-boxes-data = %{version}-%{release}
Requires: gnome-boxes-libexec = %{version}-%{release}
Requires: gnome-boxes-license = %{version}-%{release}

%description bin
bin components for the gnome-boxes package.


%package data
Summary: data components for the gnome-boxes package.
Group: Data

%description data
data components for the gnome-boxes package.


%package dev
Summary: dev components for the gnome-boxes package.
Group: Development
Requires: gnome-boxes-lib = %{version}-%{release}
Requires: gnome-boxes-bin = %{version}-%{release}
Requires: gnome-boxes-data = %{version}-%{release}
Provides: gnome-boxes-devel = %{version}-%{release}
Requires: gnome-boxes = %{version}-%{release}

%description dev
dev components for the gnome-boxes package.


%package doc
Summary: doc components for the gnome-boxes package.
Group: Documentation

%description doc
doc components for the gnome-boxes package.


%package lib
Summary: lib components for the gnome-boxes package.
Group: Libraries
Requires: gnome-boxes-data = %{version}-%{release}
Requires: gnome-boxes-libexec = %{version}-%{release}
Requires: gnome-boxes-license = %{version}-%{release}

%description lib
lib components for the gnome-boxes package.


%package libexec
Summary: libexec components for the gnome-boxes package.
Group: Default
Requires: gnome-boxes-license = %{version}-%{release}

%description libexec
libexec components for the gnome-boxes package.


%package license
Summary: license components for the gnome-boxes package.
Group: Default

%description license
license components for the gnome-boxes package.


%package locales
Summary: locales components for the gnome-boxes package.
Group: Default

%description locales
locales components for the gnome-boxes package.


%prep
%setup -q -n gnome-boxes-44.0
cd %{_builddir}/gnome-boxes-44.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679686351
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-boxes
cp %{_builddir}/gnome-boxes-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-boxes/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
cp %{_builddir}/gnome-boxes-%{version}/copyright %{buildroot}/usr/share/package-licenses/gnome-boxes/a4c835de9e0708234c05f918157e7b47ac65cde7 || :
cp %{_builddir}/gnome-boxes-%{version}/subprojects/libovf-glib/COPYING %{buildroot}/usr/share/package-licenses/gnome-boxes/3704f4680301a60004b20f94e0b5b8c7ff1484a9 || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-boxes

%files
%defattr(-,root,root,-)
/usr/lib64/gnome-boxes/girepository-1.0/Govf-0.1.typelib
/usr/lib64/gnome-boxes/pkgconfig/govf-0.1.pc

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-boxes

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Boxes.desktop
/usr/share/dbus-1/services/org.gnome.Boxes.SearchProvider.service
/usr/share/dbus-1/services/org.gnome.Boxes.service
/usr/share/glib-2.0/schemas/org.gnome.boxes.gschema.xml
/usr/share/gnome-boxes/gir-1.0/Govf-0.1.gir
/usr/share/gnome-boxes/osinfo/os/archlinux.org/archlinux-rolling.xml
/usr/share/gnome-boxes/osinfo/os/centos.org/centos-7.0.xml
/usr/share/gnome-boxes/osinfo/os/centos.org/centos-stream-9.xml
/usr/share/gnome-boxes/osinfo/os/debian.org/debian-4.xml
/usr/share/gnome-boxes/osinfo/os/endlessos.com/eos-3.3.xml
/usr/share/gnome-boxes/osinfo/os/fedoraproject.org/fedora-1.xml
/usr/share/gnome-boxes/osinfo/os/fedoraproject.org/silverblue-28.xml
/usr/share/gnome-boxes/osinfo/os/freedos.org/freedos-1.2.xml
/usr/share/gnome-boxes/osinfo/os/gnome.org/gnome-3.38.xml
/usr/share/gnome-boxes/osinfo/os/gnome.org/gnome-nightly.xml
/usr/share/gnome-boxes/osinfo/os/guix.gnu.org/guix-1.3.xml
/usr/share/gnome-boxes/osinfo/os/manjaro.org/manjaro-19.0.xml
/usr/share/gnome-boxes/osinfo/os/nixos.org/nixos-20.03.xml
/usr/share/gnome-boxes/osinfo/os/opensuse.org/opensuse-10.2.xml
/usr/share/gnome-boxes/osinfo/os/redhat.com/rhel-8.0.xml
/usr/share/gnome-boxes/osinfo/os/rockylinux.org/rocky-8.4.xml
/usr/share/gnome-boxes/osinfo/os/system76.com/popos-17.10.xml
/usr/share/gnome-boxes/osinfo/os/ubuntu.com/ubuntu-4.10.xml
/usr/share/gnome-boxes/sources/QEMU_Session
/usr/share/gnome-boxes/unattended/disk.img
/usr/share/gnome-boxes/vapi/govf-0.1.deps
/usr/share/gnome-boxes/vapi/govf-0.1.vapi
/usr/share/gnome-shell/search-providers/org.gnome.Boxes.SearchProvider.ini
/usr/share/icons/hicolor/scalable/apps/org.gnome.Boxes.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Boxes-symbolic.svg
/usr/share/metainfo/org.gnome.Boxes.appdata.xml

%files dev
%defattr(-,root,root,-)
/usr/include/gnome-boxes/govf/govf-disk.h
/usr/include/gnome-boxes/govf/govf-package.h
/usr/include/gnome-boxes/govf/govf.h

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/gnome-boxes/3d-acceleration.page
/usr/share/help/C/gnome-boxes/backup.page
/usr/share/help/C/gnome-boxes/create.page
/usr/share/help/C/gnome-boxes/delete.page
/usr/share/help/C/gnome-boxes/disk-images.page
/usr/share/help/C/gnome-boxes/edit-domain.page
/usr/share/help/C/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/C/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/C/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/C/gnome-boxes/index.page
/usr/share/help/C/gnome-boxes/install-guest-agent.page
/usr/share/help/C/gnome-boxes/interface.page
/usr/share/help/C/gnome-boxes/keystrokes.page
/usr/share/help/C/gnome-boxes/legal.xml
/usr/share/help/C/gnome-boxes/prop-system.page
/usr/share/help/C/gnome-boxes/prop-trouble.page
/usr/share/help/C/gnome-boxes/search.page
/usr/share/help/C/gnome-boxes/shared-folders.page
/usr/share/help/C/gnome-boxes/shutdown.page
/usr/share/help/C/gnome-boxes/snapshot-create.page
/usr/share/help/C/gnome-boxes/snapshot-delete.page
/usr/share/help/C/gnome-boxes/snapshot-rename.page
/usr/share/help/C/gnome-boxes/snapshot-revert.page
/usr/share/help/C/gnome-boxes/supported-protocols.page
/usr/share/help/C/gnome-boxes/system-requirements.page
/usr/share/help/C/gnome-boxes/usb-redirection.page
/usr/share/help/C/gnome-boxes/virtualization.page
/usr/share/help/C/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/C/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/ca/gnome-boxes/3d-acceleration.page
/usr/share/help/ca/gnome-boxes/backup.page
/usr/share/help/ca/gnome-boxes/create.page
/usr/share/help/ca/gnome-boxes/delete.page
/usr/share/help/ca/gnome-boxes/disk-images.page
/usr/share/help/ca/gnome-boxes/edit-domain.page
/usr/share/help/ca/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/ca/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/ca/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/ca/gnome-boxes/index.page
/usr/share/help/ca/gnome-boxes/install-guest-agent.page
/usr/share/help/ca/gnome-boxes/interface.page
/usr/share/help/ca/gnome-boxes/keystrokes.page
/usr/share/help/ca/gnome-boxes/legal.xml
/usr/share/help/ca/gnome-boxes/prop-system.page
/usr/share/help/ca/gnome-boxes/prop-trouble.page
/usr/share/help/ca/gnome-boxes/search.page
/usr/share/help/ca/gnome-boxes/shared-folders.page
/usr/share/help/ca/gnome-boxes/shutdown.page
/usr/share/help/ca/gnome-boxes/snapshot-create.page
/usr/share/help/ca/gnome-boxes/snapshot-delete.page
/usr/share/help/ca/gnome-boxes/snapshot-rename.page
/usr/share/help/ca/gnome-boxes/snapshot-revert.page
/usr/share/help/ca/gnome-boxes/supported-protocols.page
/usr/share/help/ca/gnome-boxes/system-requirements.page
/usr/share/help/ca/gnome-boxes/usb-redirection.page
/usr/share/help/ca/gnome-boxes/virtualization.page
/usr/share/help/ca/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/ca/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/cs/gnome-boxes/3d-acceleration.page
/usr/share/help/cs/gnome-boxes/backup.page
/usr/share/help/cs/gnome-boxes/create.page
/usr/share/help/cs/gnome-boxes/delete.page
/usr/share/help/cs/gnome-boxes/disk-images.page
/usr/share/help/cs/gnome-boxes/edit-domain.page
/usr/share/help/cs/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/cs/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/cs/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/cs/gnome-boxes/index.page
/usr/share/help/cs/gnome-boxes/install-guest-agent.page
/usr/share/help/cs/gnome-boxes/interface.page
/usr/share/help/cs/gnome-boxes/keystrokes.page
/usr/share/help/cs/gnome-boxes/legal.xml
/usr/share/help/cs/gnome-boxes/prop-system.page
/usr/share/help/cs/gnome-boxes/prop-trouble.page
/usr/share/help/cs/gnome-boxes/search.page
/usr/share/help/cs/gnome-boxes/shared-folders.page
/usr/share/help/cs/gnome-boxes/shutdown.page
/usr/share/help/cs/gnome-boxes/snapshot-create.page
/usr/share/help/cs/gnome-boxes/snapshot-delete.page
/usr/share/help/cs/gnome-boxes/snapshot-rename.page
/usr/share/help/cs/gnome-boxes/snapshot-revert.page
/usr/share/help/cs/gnome-boxes/supported-protocols.page
/usr/share/help/cs/gnome-boxes/system-requirements.page
/usr/share/help/cs/gnome-boxes/usb-redirection.page
/usr/share/help/cs/gnome-boxes/virtualization.page
/usr/share/help/cs/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/cs/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/da/gnome-boxes/3d-acceleration.page
/usr/share/help/da/gnome-boxes/backup.page
/usr/share/help/da/gnome-boxes/create.page
/usr/share/help/da/gnome-boxes/delete.page
/usr/share/help/da/gnome-boxes/disk-images.page
/usr/share/help/da/gnome-boxes/edit-domain.page
/usr/share/help/da/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/da/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/da/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/da/gnome-boxes/index.page
/usr/share/help/da/gnome-boxes/install-guest-agent.page
/usr/share/help/da/gnome-boxes/interface.page
/usr/share/help/da/gnome-boxes/keystrokes.page
/usr/share/help/da/gnome-boxes/legal.xml
/usr/share/help/da/gnome-boxes/prop-system.page
/usr/share/help/da/gnome-boxes/prop-trouble.page
/usr/share/help/da/gnome-boxes/search.page
/usr/share/help/da/gnome-boxes/shared-folders.page
/usr/share/help/da/gnome-boxes/shutdown.page
/usr/share/help/da/gnome-boxes/snapshot-create.page
/usr/share/help/da/gnome-boxes/snapshot-delete.page
/usr/share/help/da/gnome-boxes/snapshot-rename.page
/usr/share/help/da/gnome-boxes/snapshot-revert.page
/usr/share/help/da/gnome-boxes/supported-protocols.page
/usr/share/help/da/gnome-boxes/system-requirements.page
/usr/share/help/da/gnome-boxes/usb-redirection.page
/usr/share/help/da/gnome-boxes/virtualization.page
/usr/share/help/da/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/da/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/de/gnome-boxes/3d-acceleration.page
/usr/share/help/de/gnome-boxes/backup.page
/usr/share/help/de/gnome-boxes/create.page
/usr/share/help/de/gnome-boxes/delete.page
/usr/share/help/de/gnome-boxes/disk-images.page
/usr/share/help/de/gnome-boxes/edit-domain.page
/usr/share/help/de/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/de/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/de/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/de/gnome-boxes/index.page
/usr/share/help/de/gnome-boxes/install-guest-agent.page
/usr/share/help/de/gnome-boxes/interface.page
/usr/share/help/de/gnome-boxes/keystrokes.page
/usr/share/help/de/gnome-boxes/legal.xml
/usr/share/help/de/gnome-boxes/prop-system.page
/usr/share/help/de/gnome-boxes/prop-trouble.page
/usr/share/help/de/gnome-boxes/search.page
/usr/share/help/de/gnome-boxes/shared-folders.page
/usr/share/help/de/gnome-boxes/shutdown.page
/usr/share/help/de/gnome-boxes/snapshot-create.page
/usr/share/help/de/gnome-boxes/snapshot-delete.page
/usr/share/help/de/gnome-boxes/snapshot-rename.page
/usr/share/help/de/gnome-boxes/snapshot-revert.page
/usr/share/help/de/gnome-boxes/supported-protocols.page
/usr/share/help/de/gnome-boxes/system-requirements.page
/usr/share/help/de/gnome-boxes/usb-redirection.page
/usr/share/help/de/gnome-boxes/virtualization.page
/usr/share/help/de/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/de/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/el/gnome-boxes/3d-acceleration.page
/usr/share/help/el/gnome-boxes/backup.page
/usr/share/help/el/gnome-boxes/create.page
/usr/share/help/el/gnome-boxes/delete.page
/usr/share/help/el/gnome-boxes/disk-images.page
/usr/share/help/el/gnome-boxes/edit-domain.page
/usr/share/help/el/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/el/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/el/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/el/gnome-boxes/index.page
/usr/share/help/el/gnome-boxes/install-guest-agent.page
/usr/share/help/el/gnome-boxes/interface.page
/usr/share/help/el/gnome-boxes/keystrokes.page
/usr/share/help/el/gnome-boxes/legal.xml
/usr/share/help/el/gnome-boxes/prop-system.page
/usr/share/help/el/gnome-boxes/prop-trouble.page
/usr/share/help/el/gnome-boxes/search.page
/usr/share/help/el/gnome-boxes/shared-folders.page
/usr/share/help/el/gnome-boxes/shutdown.page
/usr/share/help/el/gnome-boxes/snapshot-create.page
/usr/share/help/el/gnome-boxes/snapshot-delete.page
/usr/share/help/el/gnome-boxes/snapshot-rename.page
/usr/share/help/el/gnome-boxes/snapshot-revert.page
/usr/share/help/el/gnome-boxes/supported-protocols.page
/usr/share/help/el/gnome-boxes/system-requirements.page
/usr/share/help/el/gnome-boxes/usb-redirection.page
/usr/share/help/el/gnome-boxes/virtualization.page
/usr/share/help/el/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/el/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/es/gnome-boxes/3d-acceleration.page
/usr/share/help/es/gnome-boxes/backup.page
/usr/share/help/es/gnome-boxes/create.page
/usr/share/help/es/gnome-boxes/delete.page
/usr/share/help/es/gnome-boxes/disk-images.page
/usr/share/help/es/gnome-boxes/edit-domain.page
/usr/share/help/es/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/es/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/es/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/es/gnome-boxes/index.page
/usr/share/help/es/gnome-boxes/install-guest-agent.page
/usr/share/help/es/gnome-boxes/interface.page
/usr/share/help/es/gnome-boxes/keystrokes.page
/usr/share/help/es/gnome-boxes/legal.xml
/usr/share/help/es/gnome-boxes/prop-system.page
/usr/share/help/es/gnome-boxes/prop-trouble.page
/usr/share/help/es/gnome-boxes/search.page
/usr/share/help/es/gnome-boxes/shared-folders.page
/usr/share/help/es/gnome-boxes/shutdown.page
/usr/share/help/es/gnome-boxes/snapshot-create.page
/usr/share/help/es/gnome-boxes/snapshot-delete.page
/usr/share/help/es/gnome-boxes/snapshot-rename.page
/usr/share/help/es/gnome-boxes/snapshot-revert.page
/usr/share/help/es/gnome-boxes/supported-protocols.page
/usr/share/help/es/gnome-boxes/system-requirements.page
/usr/share/help/es/gnome-boxes/usb-redirection.page
/usr/share/help/es/gnome-boxes/virtualization.page
/usr/share/help/es/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/es/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/eu/gnome-boxes/3d-acceleration.page
/usr/share/help/eu/gnome-boxes/backup.page
/usr/share/help/eu/gnome-boxes/create.page
/usr/share/help/eu/gnome-boxes/delete.page
/usr/share/help/eu/gnome-boxes/disk-images.page
/usr/share/help/eu/gnome-boxes/edit-domain.page
/usr/share/help/eu/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/eu/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/eu/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/eu/gnome-boxes/index.page
/usr/share/help/eu/gnome-boxes/install-guest-agent.page
/usr/share/help/eu/gnome-boxes/interface.page
/usr/share/help/eu/gnome-boxes/keystrokes.page
/usr/share/help/eu/gnome-boxes/legal.xml
/usr/share/help/eu/gnome-boxes/prop-system.page
/usr/share/help/eu/gnome-boxes/prop-trouble.page
/usr/share/help/eu/gnome-boxes/search.page
/usr/share/help/eu/gnome-boxes/shared-folders.page
/usr/share/help/eu/gnome-boxes/shutdown.page
/usr/share/help/eu/gnome-boxes/snapshot-create.page
/usr/share/help/eu/gnome-boxes/snapshot-delete.page
/usr/share/help/eu/gnome-boxes/snapshot-rename.page
/usr/share/help/eu/gnome-boxes/snapshot-revert.page
/usr/share/help/eu/gnome-boxes/supported-protocols.page
/usr/share/help/eu/gnome-boxes/system-requirements.page
/usr/share/help/eu/gnome-boxes/usb-redirection.page
/usr/share/help/eu/gnome-boxes/virtualization.page
/usr/share/help/eu/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/eu/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/fr/gnome-boxes/3d-acceleration.page
/usr/share/help/fr/gnome-boxes/backup.page
/usr/share/help/fr/gnome-boxes/create.page
/usr/share/help/fr/gnome-boxes/delete.page
/usr/share/help/fr/gnome-boxes/disk-images.page
/usr/share/help/fr/gnome-boxes/edit-domain.page
/usr/share/help/fr/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/fr/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/fr/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/fr/gnome-boxes/index.page
/usr/share/help/fr/gnome-boxes/install-guest-agent.page
/usr/share/help/fr/gnome-boxes/interface.page
/usr/share/help/fr/gnome-boxes/keystrokes.page
/usr/share/help/fr/gnome-boxes/legal.xml
/usr/share/help/fr/gnome-boxes/prop-system.page
/usr/share/help/fr/gnome-boxes/prop-trouble.page
/usr/share/help/fr/gnome-boxes/search.page
/usr/share/help/fr/gnome-boxes/shared-folders.page
/usr/share/help/fr/gnome-boxes/shutdown.page
/usr/share/help/fr/gnome-boxes/snapshot-create.page
/usr/share/help/fr/gnome-boxes/snapshot-delete.page
/usr/share/help/fr/gnome-boxes/snapshot-rename.page
/usr/share/help/fr/gnome-boxes/snapshot-revert.page
/usr/share/help/fr/gnome-boxes/supported-protocols.page
/usr/share/help/fr/gnome-boxes/system-requirements.page
/usr/share/help/fr/gnome-boxes/usb-redirection.page
/usr/share/help/fr/gnome-boxes/virtualization.page
/usr/share/help/fr/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/fr/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/gl/gnome-boxes/3d-acceleration.page
/usr/share/help/gl/gnome-boxes/backup.page
/usr/share/help/gl/gnome-boxes/create.page
/usr/share/help/gl/gnome-boxes/delete.page
/usr/share/help/gl/gnome-boxes/disk-images.page
/usr/share/help/gl/gnome-boxes/edit-domain.page
/usr/share/help/gl/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/gl/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/gl/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/gl/gnome-boxes/index.page
/usr/share/help/gl/gnome-boxes/install-guest-agent.page
/usr/share/help/gl/gnome-boxes/interface.page
/usr/share/help/gl/gnome-boxes/keystrokes.page
/usr/share/help/gl/gnome-boxes/legal.xml
/usr/share/help/gl/gnome-boxes/prop-system.page
/usr/share/help/gl/gnome-boxes/prop-trouble.page
/usr/share/help/gl/gnome-boxes/search.page
/usr/share/help/gl/gnome-boxes/shared-folders.page
/usr/share/help/gl/gnome-boxes/shutdown.page
/usr/share/help/gl/gnome-boxes/snapshot-create.page
/usr/share/help/gl/gnome-boxes/snapshot-delete.page
/usr/share/help/gl/gnome-boxes/snapshot-rename.page
/usr/share/help/gl/gnome-boxes/snapshot-revert.page
/usr/share/help/gl/gnome-boxes/supported-protocols.page
/usr/share/help/gl/gnome-boxes/system-requirements.page
/usr/share/help/gl/gnome-boxes/usb-redirection.page
/usr/share/help/gl/gnome-boxes/virtualization.page
/usr/share/help/gl/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/gl/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/hu/gnome-boxes/3d-acceleration.page
/usr/share/help/hu/gnome-boxes/backup.page
/usr/share/help/hu/gnome-boxes/create.page
/usr/share/help/hu/gnome-boxes/delete.page
/usr/share/help/hu/gnome-boxes/disk-images.page
/usr/share/help/hu/gnome-boxes/edit-domain.page
/usr/share/help/hu/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/hu/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/hu/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/hu/gnome-boxes/index.page
/usr/share/help/hu/gnome-boxes/install-guest-agent.page
/usr/share/help/hu/gnome-boxes/interface.page
/usr/share/help/hu/gnome-boxes/keystrokes.page
/usr/share/help/hu/gnome-boxes/legal.xml
/usr/share/help/hu/gnome-boxes/prop-system.page
/usr/share/help/hu/gnome-boxes/prop-trouble.page
/usr/share/help/hu/gnome-boxes/search.page
/usr/share/help/hu/gnome-boxes/shared-folders.page
/usr/share/help/hu/gnome-boxes/shutdown.page
/usr/share/help/hu/gnome-boxes/snapshot-create.page
/usr/share/help/hu/gnome-boxes/snapshot-delete.page
/usr/share/help/hu/gnome-boxes/snapshot-rename.page
/usr/share/help/hu/gnome-boxes/snapshot-revert.page
/usr/share/help/hu/gnome-boxes/supported-protocols.page
/usr/share/help/hu/gnome-boxes/system-requirements.page
/usr/share/help/hu/gnome-boxes/usb-redirection.page
/usr/share/help/hu/gnome-boxes/virtualization.page
/usr/share/help/hu/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/hu/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/id/gnome-boxes/3d-acceleration.page
/usr/share/help/id/gnome-boxes/backup.page
/usr/share/help/id/gnome-boxes/create.page
/usr/share/help/id/gnome-boxes/delete.page
/usr/share/help/id/gnome-boxes/disk-images.page
/usr/share/help/id/gnome-boxes/edit-domain.page
/usr/share/help/id/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/id/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/id/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/id/gnome-boxes/index.page
/usr/share/help/id/gnome-boxes/install-guest-agent.page
/usr/share/help/id/gnome-boxes/interface.page
/usr/share/help/id/gnome-boxes/keystrokes.page
/usr/share/help/id/gnome-boxes/legal.xml
/usr/share/help/id/gnome-boxes/prop-system.page
/usr/share/help/id/gnome-boxes/prop-trouble.page
/usr/share/help/id/gnome-boxes/search.page
/usr/share/help/id/gnome-boxes/shared-folders.page
/usr/share/help/id/gnome-boxes/shutdown.page
/usr/share/help/id/gnome-boxes/snapshot-create.page
/usr/share/help/id/gnome-boxes/snapshot-delete.page
/usr/share/help/id/gnome-boxes/snapshot-rename.page
/usr/share/help/id/gnome-boxes/snapshot-revert.page
/usr/share/help/id/gnome-boxes/supported-protocols.page
/usr/share/help/id/gnome-boxes/system-requirements.page
/usr/share/help/id/gnome-boxes/usb-redirection.page
/usr/share/help/id/gnome-boxes/virtualization.page
/usr/share/help/id/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/id/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/it/gnome-boxes/3d-acceleration.page
/usr/share/help/it/gnome-boxes/backup.page
/usr/share/help/it/gnome-boxes/create.page
/usr/share/help/it/gnome-boxes/delete.page
/usr/share/help/it/gnome-boxes/disk-images.page
/usr/share/help/it/gnome-boxes/edit-domain.page
/usr/share/help/it/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/it/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/it/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/it/gnome-boxes/index.page
/usr/share/help/it/gnome-boxes/install-guest-agent.page
/usr/share/help/it/gnome-boxes/interface.page
/usr/share/help/it/gnome-boxes/keystrokes.page
/usr/share/help/it/gnome-boxes/legal.xml
/usr/share/help/it/gnome-boxes/prop-system.page
/usr/share/help/it/gnome-boxes/prop-trouble.page
/usr/share/help/it/gnome-boxes/search.page
/usr/share/help/it/gnome-boxes/shared-folders.page
/usr/share/help/it/gnome-boxes/shutdown.page
/usr/share/help/it/gnome-boxes/snapshot-create.page
/usr/share/help/it/gnome-boxes/snapshot-delete.page
/usr/share/help/it/gnome-boxes/snapshot-rename.page
/usr/share/help/it/gnome-boxes/snapshot-revert.page
/usr/share/help/it/gnome-boxes/supported-protocols.page
/usr/share/help/it/gnome-boxes/system-requirements.page
/usr/share/help/it/gnome-boxes/usb-redirection.page
/usr/share/help/it/gnome-boxes/virtualization.page
/usr/share/help/it/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/it/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/ko/gnome-boxes/3d-acceleration.page
/usr/share/help/ko/gnome-boxes/backup.page
/usr/share/help/ko/gnome-boxes/create.page
/usr/share/help/ko/gnome-boxes/delete.page
/usr/share/help/ko/gnome-boxes/disk-images.page
/usr/share/help/ko/gnome-boxes/edit-domain.page
/usr/share/help/ko/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/ko/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/ko/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/ko/gnome-boxes/index.page
/usr/share/help/ko/gnome-boxes/install-guest-agent.page
/usr/share/help/ko/gnome-boxes/interface.page
/usr/share/help/ko/gnome-boxes/keystrokes.page
/usr/share/help/ko/gnome-boxes/legal.xml
/usr/share/help/ko/gnome-boxes/prop-system.page
/usr/share/help/ko/gnome-boxes/prop-trouble.page
/usr/share/help/ko/gnome-boxes/search.page
/usr/share/help/ko/gnome-boxes/shared-folders.page
/usr/share/help/ko/gnome-boxes/shutdown.page
/usr/share/help/ko/gnome-boxes/snapshot-create.page
/usr/share/help/ko/gnome-boxes/snapshot-delete.page
/usr/share/help/ko/gnome-boxes/snapshot-rename.page
/usr/share/help/ko/gnome-boxes/snapshot-revert.page
/usr/share/help/ko/gnome-boxes/supported-protocols.page
/usr/share/help/ko/gnome-boxes/system-requirements.page
/usr/share/help/ko/gnome-boxes/usb-redirection.page
/usr/share/help/ko/gnome-boxes/virtualization.page
/usr/share/help/ko/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/ko/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/pl/gnome-boxes/3d-acceleration.page
/usr/share/help/pl/gnome-boxes/backup.page
/usr/share/help/pl/gnome-boxes/create.page
/usr/share/help/pl/gnome-boxes/delete.page
/usr/share/help/pl/gnome-boxes/disk-images.page
/usr/share/help/pl/gnome-boxes/edit-domain.page
/usr/share/help/pl/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/pl/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/pl/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/pl/gnome-boxes/index.page
/usr/share/help/pl/gnome-boxes/install-guest-agent.page
/usr/share/help/pl/gnome-boxes/interface.page
/usr/share/help/pl/gnome-boxes/keystrokes.page
/usr/share/help/pl/gnome-boxes/legal.xml
/usr/share/help/pl/gnome-boxes/prop-system.page
/usr/share/help/pl/gnome-boxes/prop-trouble.page
/usr/share/help/pl/gnome-boxes/search.page
/usr/share/help/pl/gnome-boxes/shared-folders.page
/usr/share/help/pl/gnome-boxes/shutdown.page
/usr/share/help/pl/gnome-boxes/snapshot-create.page
/usr/share/help/pl/gnome-boxes/snapshot-delete.page
/usr/share/help/pl/gnome-boxes/snapshot-rename.page
/usr/share/help/pl/gnome-boxes/snapshot-revert.page
/usr/share/help/pl/gnome-boxes/supported-protocols.page
/usr/share/help/pl/gnome-boxes/system-requirements.page
/usr/share/help/pl/gnome-boxes/usb-redirection.page
/usr/share/help/pl/gnome-boxes/virtualization.page
/usr/share/help/pl/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/pl/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/pt_BR/gnome-boxes/3d-acceleration.page
/usr/share/help/pt_BR/gnome-boxes/backup.page
/usr/share/help/pt_BR/gnome-boxes/create.page
/usr/share/help/pt_BR/gnome-boxes/delete.page
/usr/share/help/pt_BR/gnome-boxes/disk-images.page
/usr/share/help/pt_BR/gnome-boxes/edit-domain.page
/usr/share/help/pt_BR/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/pt_BR/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/pt_BR/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/pt_BR/gnome-boxes/index.page
/usr/share/help/pt_BR/gnome-boxes/install-guest-agent.page
/usr/share/help/pt_BR/gnome-boxes/interface.page
/usr/share/help/pt_BR/gnome-boxes/keystrokes.page
/usr/share/help/pt_BR/gnome-boxes/legal.xml
/usr/share/help/pt_BR/gnome-boxes/prop-system.page
/usr/share/help/pt_BR/gnome-boxes/prop-trouble.page
/usr/share/help/pt_BR/gnome-boxes/search.page
/usr/share/help/pt_BR/gnome-boxes/shared-folders.page
/usr/share/help/pt_BR/gnome-boxes/shutdown.page
/usr/share/help/pt_BR/gnome-boxes/snapshot-create.page
/usr/share/help/pt_BR/gnome-boxes/snapshot-delete.page
/usr/share/help/pt_BR/gnome-boxes/snapshot-rename.page
/usr/share/help/pt_BR/gnome-boxes/snapshot-revert.page
/usr/share/help/pt_BR/gnome-boxes/supported-protocols.page
/usr/share/help/pt_BR/gnome-boxes/system-requirements.page
/usr/share/help/pt_BR/gnome-boxes/usb-redirection.page
/usr/share/help/pt_BR/gnome-boxes/virtualization.page
/usr/share/help/pt_BR/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/pt_BR/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/ru/gnome-boxes/3d-acceleration.page
/usr/share/help/ru/gnome-boxes/backup.page
/usr/share/help/ru/gnome-boxes/create.page
/usr/share/help/ru/gnome-boxes/delete.page
/usr/share/help/ru/gnome-boxes/disk-images.page
/usr/share/help/ru/gnome-boxes/edit-domain.page
/usr/share/help/ru/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/ru/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/ru/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/ru/gnome-boxes/index.page
/usr/share/help/ru/gnome-boxes/install-guest-agent.page
/usr/share/help/ru/gnome-boxes/interface.page
/usr/share/help/ru/gnome-boxes/keystrokes.page
/usr/share/help/ru/gnome-boxes/legal.xml
/usr/share/help/ru/gnome-boxes/prop-system.page
/usr/share/help/ru/gnome-boxes/prop-trouble.page
/usr/share/help/ru/gnome-boxes/search.page
/usr/share/help/ru/gnome-boxes/shared-folders.page
/usr/share/help/ru/gnome-boxes/shutdown.page
/usr/share/help/ru/gnome-boxes/snapshot-create.page
/usr/share/help/ru/gnome-boxes/snapshot-delete.page
/usr/share/help/ru/gnome-boxes/snapshot-rename.page
/usr/share/help/ru/gnome-boxes/snapshot-revert.page
/usr/share/help/ru/gnome-boxes/supported-protocols.page
/usr/share/help/ru/gnome-boxes/system-requirements.page
/usr/share/help/ru/gnome-boxes/usb-redirection.page
/usr/share/help/ru/gnome-boxes/virtualization.page
/usr/share/help/ru/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/ru/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/sv/gnome-boxes/3d-acceleration.page
/usr/share/help/sv/gnome-boxes/backup.page
/usr/share/help/sv/gnome-boxes/create.page
/usr/share/help/sv/gnome-boxes/delete.page
/usr/share/help/sv/gnome-boxes/disk-images.page
/usr/share/help/sv/gnome-boxes/edit-domain.page
/usr/share/help/sv/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/sv/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/sv/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/sv/gnome-boxes/index.page
/usr/share/help/sv/gnome-boxes/install-guest-agent.page
/usr/share/help/sv/gnome-boxes/interface.page
/usr/share/help/sv/gnome-boxes/keystrokes.page
/usr/share/help/sv/gnome-boxes/legal.xml
/usr/share/help/sv/gnome-boxes/prop-system.page
/usr/share/help/sv/gnome-boxes/prop-trouble.page
/usr/share/help/sv/gnome-boxes/search.page
/usr/share/help/sv/gnome-boxes/shared-folders.page
/usr/share/help/sv/gnome-boxes/shutdown.page
/usr/share/help/sv/gnome-boxes/snapshot-create.page
/usr/share/help/sv/gnome-boxes/snapshot-delete.page
/usr/share/help/sv/gnome-boxes/snapshot-rename.page
/usr/share/help/sv/gnome-boxes/snapshot-revert.page
/usr/share/help/sv/gnome-boxes/supported-protocols.page
/usr/share/help/sv/gnome-boxes/system-requirements.page
/usr/share/help/sv/gnome-boxes/usb-redirection.page
/usr/share/help/sv/gnome-boxes/virtualization.page
/usr/share/help/sv/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/sv/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/tr/gnome-boxes/3d-acceleration.page
/usr/share/help/tr/gnome-boxes/backup.page
/usr/share/help/tr/gnome-boxes/create.page
/usr/share/help/tr/gnome-boxes/delete.page
/usr/share/help/tr/gnome-boxes/disk-images.page
/usr/share/help/tr/gnome-boxes/edit-domain.page
/usr/share/help/tr/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/tr/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/tr/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/tr/gnome-boxes/index.page
/usr/share/help/tr/gnome-boxes/install-guest-agent.page
/usr/share/help/tr/gnome-boxes/interface.page
/usr/share/help/tr/gnome-boxes/keystrokes.page
/usr/share/help/tr/gnome-boxes/legal.xml
/usr/share/help/tr/gnome-boxes/prop-system.page
/usr/share/help/tr/gnome-boxes/prop-trouble.page
/usr/share/help/tr/gnome-boxes/search.page
/usr/share/help/tr/gnome-boxes/shared-folders.page
/usr/share/help/tr/gnome-boxes/shutdown.page
/usr/share/help/tr/gnome-boxes/snapshot-create.page
/usr/share/help/tr/gnome-boxes/snapshot-delete.page
/usr/share/help/tr/gnome-boxes/snapshot-rename.page
/usr/share/help/tr/gnome-boxes/snapshot-revert.page
/usr/share/help/tr/gnome-boxes/supported-protocols.page
/usr/share/help/tr/gnome-boxes/system-requirements.page
/usr/share/help/tr/gnome-boxes/usb-redirection.page
/usr/share/help/tr/gnome-boxes/virtualization.page
/usr/share/help/tr/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/tr/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/uk/gnome-boxes/3d-acceleration.page
/usr/share/help/uk/gnome-boxes/backup.page
/usr/share/help/uk/gnome-boxes/create.page
/usr/share/help/uk/gnome-boxes/delete.page
/usr/share/help/uk/gnome-boxes/disk-images.page
/usr/share/help/uk/gnome-boxes/edit-domain.page
/usr/share/help/uk/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/uk/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/uk/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/uk/gnome-boxes/index.page
/usr/share/help/uk/gnome-boxes/install-guest-agent.page
/usr/share/help/uk/gnome-boxes/interface.page
/usr/share/help/uk/gnome-boxes/keystrokes.page
/usr/share/help/uk/gnome-boxes/legal.xml
/usr/share/help/uk/gnome-boxes/prop-system.page
/usr/share/help/uk/gnome-boxes/prop-trouble.page
/usr/share/help/uk/gnome-boxes/search.page
/usr/share/help/uk/gnome-boxes/shared-folders.page
/usr/share/help/uk/gnome-boxes/shutdown.page
/usr/share/help/uk/gnome-boxes/snapshot-create.page
/usr/share/help/uk/gnome-boxes/snapshot-delete.page
/usr/share/help/uk/gnome-boxes/snapshot-rename.page
/usr/share/help/uk/gnome-boxes/snapshot-revert.page
/usr/share/help/uk/gnome-boxes/supported-protocols.page
/usr/share/help/uk/gnome-boxes/system-requirements.page
/usr/share/help/uk/gnome-boxes/usb-redirection.page
/usr/share/help/uk/gnome-boxes/virtualization.page
/usr/share/help/uk/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/uk/gnome-boxes/why-do-i-need-virtual-machine.page
/usr/share/help/zh_CN/gnome-boxes/3d-acceleration.page
/usr/share/help/zh_CN/gnome-boxes/backup.page
/usr/share/help/zh_CN/gnome-boxes/create.page
/usr/share/help/zh_CN/gnome-boxes/delete.page
/usr/share/help/zh_CN/gnome-boxes/disk-images.page
/usr/share/help/zh_CN/gnome-boxes/edit-domain.page
/usr/share/help/zh_CN/gnome-boxes/figures/boxes_icon.svg
/usr/share/help/zh_CN/gnome-boxes/figures/input-keyboard-symbolic.svg
/usr/share/help/zh_CN/gnome-boxes/figures/view-more-symbolic.svg
/usr/share/help/zh_CN/gnome-boxes/index.page
/usr/share/help/zh_CN/gnome-boxes/install-guest-agent.page
/usr/share/help/zh_CN/gnome-boxes/interface.page
/usr/share/help/zh_CN/gnome-boxes/keystrokes.page
/usr/share/help/zh_CN/gnome-boxes/legal.xml
/usr/share/help/zh_CN/gnome-boxes/prop-system.page
/usr/share/help/zh_CN/gnome-boxes/prop-trouble.page
/usr/share/help/zh_CN/gnome-boxes/search.page
/usr/share/help/zh_CN/gnome-boxes/shared-folders.page
/usr/share/help/zh_CN/gnome-boxes/shutdown.page
/usr/share/help/zh_CN/gnome-boxes/snapshot-create.page
/usr/share/help/zh_CN/gnome-boxes/snapshot-delete.page
/usr/share/help/zh_CN/gnome-boxes/snapshot-rename.page
/usr/share/help/zh_CN/gnome-boxes/snapshot-revert.page
/usr/share/help/zh_CN/gnome-boxes/supported-protocols.page
/usr/share/help/zh_CN/gnome-boxes/system-requirements.page
/usr/share/help/zh_CN/gnome-boxes/usb-redirection.page
/usr/share/help/zh_CN/gnome-boxes/virtualization.page
/usr/share/help/zh_CN/gnome-boxes/what-is-a-virtual-machine.page
/usr/share/help/zh_CN/gnome-boxes/why-do-i-need-virtual-machine.page

%files lib
%defattr(-,root,root,-)
/usr/lib64/gnome-boxes/libgovf-0.1.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gnome-boxes-search-provider

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-boxes/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/gnome-boxes/a4c835de9e0708234c05f918157e7b47ac65cde7
/usr/share/package-licenses/gnome-boxes/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f gnome-boxes.lang
%defattr(-,root,root,-)

