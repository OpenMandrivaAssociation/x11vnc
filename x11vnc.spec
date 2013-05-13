Name:           x11vnc
Version:        0.9.12
Release:        3
Summary:        VNC server for the current X11 session
License:        GPL
Group:          System/X11
URL:            http://www.karlrunge.com/x11vnc/
Source:         http://downloads.sourceforge.net/sourceforge/libvncserver/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(xi)

%description
x11vnc is to X Window System what WinVNC is to Windows, i.e. a server
which serves the current X Window System desktop via RFB (VNC)
protocol to the user.

Based on the ideas of x0rfbserver and on LibVNCServer, it has evolved
into a versatile and performant while still easy to use program.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

rm -fr %buildroot%_includedir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_mandir}/man1/x11vnc.1*
%{_bindir}/x11vnc
%{_datadir}/x11vnc/
%{_datadir}/applications/x11vnc.desktop


%changelog
* Sun Nov 28 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.9.12-1mdv2011.0
+ Revision: 602291
- new version 0.9.12

* Mon Aug 09 2010 Funda Wang <fwang@mandriva.org> 0.9.11-1mdv2011.0
+ Revision: 568020
- new version 0.9.11

* Wed Jul 28 2010 Matthew Dawkins <mattydaw@mandriva.org> 0.9.10-1mdv2011.0
+ Revision: 562688
- new version 0.9.10

* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 0.9.9-2mdv2010.1
+ Revision: 533626
- rebuild

* Sat Jan 16 2010 Funda Wang <fwang@mandriva.org> 0.9.9-1mdv2010.1
+ Revision: 492118
- New version 0.9.9

* Sun Aug 23 2009 Funda Wang <fwang@mandriva.org> 0.9.8-2mdv2010.0
+ Revision: 419821
- rebulid for new libjpeg v7

* Fri Jul 10 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.8-1mdv2010.0
+ Revision: 394043
- Update to new version 0.9.8

* Tue Dec 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.6-1mdv2009.1
+ Revision: 321453
- new version
- fix format errors
- don't recompress sources

* Fri Oct 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.5-1mdv2009.1
+ Revision: 297013
- update to new version 0.9.5

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.9.3-4mdv2009.0
+ Revision: 262202
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.9.3-3mdv2009.0
+ Revision: 256487
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request
- delete old sources

* Fri Oct 12 2007 Jérôme Soyer <saispo@mandriva.org> 0.9.3-1mdv2008.1
+ Revision: 97354
- New release 0.9.3

* Fri May 25 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.1-1mdv2008.0
+ Revision: 31136
- update, and ensure use of system libvncserver


* Sun Apr 02 2006 Jerome Soyer <saispo@mandriva.org> 0.8-1mdk
- New release 0.8

* Mon Jan 16 2006 Michael Scherer <misc@mandriva.org> 0.7.2-1mdk
- initial release, based on Dag Wiers specfile
