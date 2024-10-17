Name:           x11vnc
Version:        0.9.16
Release:        2
Summary:        VNC server for the current X11 session
License:        GPLv2+
Group:          System/X11
URL:            https://www.karlrunge.com/x11vnc/
Source0:        https://github.com/LibVNC/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/LibVNC/x11vnc/pull/121.patch
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(openssl)
# for -gui
Requires:       tk

%description
What WinVNC is to Windows x11vnc is to X Window System, i.e. a server
which serves the current X Window System desktop via RFB (VNC)
protocol to the user.

Based on the ideas of x0rfbserver and on LibVNCServer it has evolved into a
versatile and productive while still easy to use program.


%prep
%setup -q
%autopatch -p1

#make autoreconf more happy
sed -i -e 's,AM_INIT_AUTOMAKE.*,AM_INIT_AUTOMAKE(\[subdir-objects\]),' configure.ac

%build
# fix build on aarch64
autoreconf -vfi

%configure --with-system-libvncserver --without-tightvnc-filetransfer
%make_build

%install
%make_install

rm -fr %buildroot%_includedir

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_mandir}/man1/x11vnc.1*
%{_bindir}/x11vnc
%{_bindir}/Xdummy
%{_datadir}/applications/x11vnc.desktop
