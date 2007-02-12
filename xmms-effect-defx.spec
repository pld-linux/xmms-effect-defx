Summary:	DeFX Multi-effects processor Plug-in for XMMS
Summary(pl.UTF-8):   Procesor efektów DeFX - wtyczka dla XMMS
Name:		xmms-effect-defx
Version:	0.9.9
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/defx/xmms-defx-%{version}.tar.gz
# Source0-md5:	89d1e2dce6fcb8eedada91891366a9ba
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

%description -l pl.UTF-8
DeFX to wtyczka do XMMS umożliwiająca uzyskanie 6 typów efektów,
pogrupowanych w 4 oddzielne moduły:
- Karaoke: usuwa głos starając się zachować resztę dźwięków,
- Panning: płynne przejścia między kanałami stereo,
- Modulacja: trzy klasyczne efekty: flange, fazer i chorus,
- Rewerbracja: symuluje odtwarzanie w dużym pomieszczeniu.

%prep
%setup -q -n xmms-defx-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="-c %{rpmcflags} -fPIC -ffast-math `gtk-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_effect_plugindir}

install lib/libdefx.so $RPM_BUILD_ROOT%{xmms_effect_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* README
%attr(755,root,root) %{xmms_effect_plugindir}/*.so
