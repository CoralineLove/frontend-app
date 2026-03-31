// parser.js
import { console } from 'console';

class XMLParser {
  constructor() {
    this.xmlDom = null;
  }

  parse(xmlString) {
    try {
      this.xmlDom = new DOMParser().parseFromString(xmlString, 'application/xml');
      return this.xmlDom;
    } catch (error) {
      console.error(error);
      return null;
    }
  }

  getElementsByTagName(tagName) {
    if (!this.xmlDom) {
      return [];
    }
    return this.xmlDom.getElementsByTagName(tagName);
  }

  getTextContent(element) {
    if (!element) {
      return '';
    }
    return element.textContent || '';
  }
}

export { XMLParser };