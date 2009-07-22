import functest
# Generated by the windmill services transformer
from windmill.authoring import WindmillTestClient

def test_ide_asserts():
    client = WindmillTestClient(__name__, assertions=False)

    assert client.open(url=u'http://tutorial.getwindmill.com/windmill-unittests/unit_tester.html')['result']
    assert client.waits.forPageLoad(timeout=u'8000')['result']
    assert client.asserts.assertImageLoaded(id=u'headerImg')['result']
    assert client.asserts.assertNotImageLoaded(id=u'imgNotLoaded')['result']
    assert not client.asserts.assertImageLoaded(id=u'imgNotLoaded')['result']
    assert not client.asserts.assertNotImageLoaded(id=u'headerImg')['result']
    assert client.asserts.assertElemJS(js=u'element.name == "animal"', id=u'cougar')['result']
    assert client.asserts.assertProperty(validator=u'style.width|200px', id=u'clickme')['result']
    assert client.asserts.assertText(validator=u'Stuff in here', id=u'stuffInside')['result']
    assert client.asserts.assertTextIn(validator=u'Stuff', id=u'stuffInside')['result']
    assert not client.asserts.assertText(validator=u'crap', id=u'stuffInside')['result']
    assert client.asserts.assertValue(validator=u'assert this value', id=u'assertVal')['result']
    assert client.asserts.assertValueIn(validator=u'this', id=u'assertVal')['result']
    assert client.asserts.assertNotValue(validator=u'asd', id=u'assertVal')['result']
    assert client.asserts.assertNotValueIn(validator=u'asd', id=u'assertVal')['result']
    assert not client.asserts.assertValue(validator=u'wrong assert', id=u'assertVal')['result']
    assert client.asserts.assertNotValue(validator=u'aasdasd', id=u'assertVal')['result']
    assert client.asserts.assertChecked(id=u'boxchecked')['result']
    assert not client.asserts.assertChecked(id=u'boxnotchecked')['result']
    assert client.asserts.assertNotChecked(id=u'boxnotchecked')['result']
    assert not client.asserts.assertNotChecked(id=u'boxchecked')['result']
    assert client.asserts.assertSelected(validator=u'Rock', id=u'assertSelected')['result']
    assert not client.asserts.assertSelected(validator=u'boom', id=u'assertSelected')['result']