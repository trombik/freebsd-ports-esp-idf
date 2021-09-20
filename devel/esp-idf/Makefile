PORTNAME=	esp-idf
DISTVERSION=	#
CATEGORIES=	devel
MASTER_SITES=	#

MAINTAINER=	y@trombik.org
COMMENT=	Official development framework for ESP32

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	\
	${PYTHON_PKGNAMEPREFIX}pip>0:devel/py-pip@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}virtualenv>=0:devel/py-virtualenv@${PY_FLAVOR} \
	rust>0:lang/rust \
	gmake>=4.3:devel/gmake

# see https://github.com/espressif/esp-idf/releases and
# https://github.com/espressif/esp-idf/blob/master/SUPPORT_POLICY.md
FLAVORS=	idf43 idf33
FLAVOR?=	${FLAVORS:[1]}

USES=	python cmake:run

idf43_PLIST=	${MASTERDIR}/pkg-plist.${FLAVOR}
idf33_PLIST=	${MASTERDIR}/pkg-plist.${FLAVOR}
idf43_PKGNAMESUFFIX=	-${FLAVOR}
idf33_PKGNAMESUFFIX=	-${FLAVOR}
DISTINFO_FILE=	${MASTERDIR}/distinfo.${FLAVOR}
PATCHDIR=	${MASTERDIR}/files/${FLAVOR}

.if ${FLAVOR} == "idf43"
DISTVERSION=	4.3.1
.elif ${FLAVOR} == "idf33"
DISTVERSION=	3.3.5
.endif

USE_GITHUB=	yes
GH_TUPLE=	espressif:${PORTNAME}:v${DISTVERSION}
NO_BUILD=	yes
SUB_FILES=	pkg-message
SUB_LIST=	PREFIX=${PREFIX} PORTNAME=${PORTNAME} PKGNAMESUFFIX=${PKGNAMESUFFIX} PYTHON_VERSION=${PYTHON_VERSION}

# do nothing. we need runtime dependency only.
do-configure:
	true

do-install:
	${INSTALL} -d ${STAGEDIR}${PREFIX}/${PORTNAME}${PKGNAMESUFFIX}
	cd ${WRKSRC} && ${COPYTREE_SHARE} . ${STAGEDIR}${PREFIX}/${PORTNAME}${PKGNAMESUFFIX}

.include <bsd.port.mk>
