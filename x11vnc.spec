Summary: VNC server for the current X11 session
Name: x11vnc
Version: 0.8
Release: %mkrel 1
License: GPL
Group: System/X11
URL: http://www.karlrunge.com/x11vnc/
Source:	http://dl.sf.net/libvncserver/x11vnc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libjpeg-devel, zlib-devel
BuildRequires: X11-devel

%description
x11vnc is to X Window System what WinVNC is to Windows, i.e. a server
which serves the current X Window System desktop via RFB (VNC)
protocol to the user.

Based on the ideas of x0rfbserver and on LibVNCServer, it has evolved
into a versatile and performant while still easy to use program.

%prep
%setup -q

%build
%configure
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_mandir}/man1/x11vnc.1*
%{_bindir}/x11vnc
%{_datadir}/x11vnc/

