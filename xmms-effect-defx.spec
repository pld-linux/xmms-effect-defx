Summary:	DeFX Multi-effects processor Plug-in for XMMS
Summary(pl):	Procesor efekt�w DeFX - wtyczka dla XMMS
Name:		xmms-effect-defx
Version:	0.9.8
Release:	3
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://defx.sourceforge.net/defx/defx-%{version}.tar.gz
# Source0-md5:	eee11e5299425b729ad7ad5a588e3906
URL:		http://defx.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DeFX is a plug-in module for XMMS. It supports 6 types of effects,
grouped into 4 different modules:
 - Karaoke: Removes the song's voices trying to preserve the bass and
   drums
 - Panning: Smoothly selects between the two stereo channels
 - Modulation: Three classical effects. Flange, phaser and chorus
 - Reverberation: You can simulate your songs as being played in a
   huge room.

%description -l pl
DeFX to wtyczka do XMMS umo�liwiaj�ca uzyskanie 6 typ�w efekt�w,
pogrupowanych w 4 oddzielne modu�y:
- Karaoke: usuwa g�os staraj�c si� zachowa� reszt� d�wi�k�w,
- Panning: p�ynne przej�cia mi�dzy kana�ami stereo,
- Modulacja: trzy klasyczne efekty: flange, fazer i chorus,
- Rewerbracja: symuluje odtwarzanie w du�ym pomieszczeniu.

%prep
%setup -q -n defx-%{version}

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="-c %{rpmcflags} -ffast-math `gtk-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT

install -D lib/defx.so $RPM_BUILD_ROOT%{xmms_effect_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* README
%attr(755,root,root) %{xmms_effect_plugindir}/*.so
