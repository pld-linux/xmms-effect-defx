Summary:	DeFX Multi-effects processor Plug-in for XMMS
Summary(pl):	DeFX procesor efekt�w - plugin dla XMMS
Name:		xmms-effect-defx
Version:	0.9.8
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://defx.sourceforge.net/defx/defx-0.9.8.tar.gz
URL:		http://defx.sourceforge.net/
Requires:	xmms
BuildRequires:	xmms-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
DeFX is a plug-in module for XMMS.
DeFX support 6 types of effects, grouped into 4 different modules.
    * Karaoke : Removes the song's voices trying to preserve the bass and drums
    * Panning : Smoothly selects between the two stereo channels
    * Modulation : Three classical effects. Flange, phaser and chorus
    * Reverberation : You can simulate your songs as being played in a huge room

%description -l pl
Wtyczka umozliwiaj�ca uzyskanie 6 typ�w efekt�w:
karaoke, panning, modulacja, reverb 

%prep
%setup -q -n defx-%{version}
%build
%{__make} \
	COMMON_CFLAGS="%{rpmcflags} \
	-ffast-math `glib-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/`%{_bindir}/xmms-config --effect-plugin-dir`/
install lib/defx.so \
	$RPM_BUILD_ROOT/`%{_bindir}/xmms-config	--effect-plugin-dir`/defx.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* README
%attr(755,root,root) %{_libdir}/xmms/*/*.so
