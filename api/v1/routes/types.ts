// frontend-app/types.ts

enum SortOrder {
  ASC = 'asc',
  DESC = 'desc',
}

enum SortField {
  DATE = 'date',
  RATING = 'rating',
  TITLE = 'title',
}

enum CardType {
  ITEM = 'item',
  CATEGORY = 'category',
  SUBCATEGORY = 'subcategory',
}

interface User {
  id: number;
  name: string;
  email: string;
  avatar: string;
  role: string;
  token: string;
}

interface Item {
  id: number;
  title: string;
  description: string;
  userID: number;
  rating: number;
  reviews: number;
  date: string;
  tags: string[];
}

interface Category {
  id: number;
  title: string;
  description: string;
  items: number[];
}

interface Subcategory {
  id: number;
  title: string;
  description: string;
  categoryID: number;
  items: number[];
}

interface Review {
  id: number;
  rating: number;
  review: string;
  itemID: number;
  userID: number;
  date: string;
}

interface Paginate {
  limit: number;
  skip: number;
  total: number;
}

interface Sort {
  field: SortField;
  order: SortOrder;
}

interface Filter {
  categoryID?: number;
  subcategoryID?: number;
  date?: string;
  rating?: number;
  title?: string;
}