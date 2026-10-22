const image_data = [
    {
        "id": 1,
        "title": "Mountain Landscape",
        "category": "Nature",
        "image_url": "https://images.unsplash.com/photo-1500534623283-312aade485b7"
    },
    {
        "id": 2,
        "title": "Forest Road",
        "category": "Nature",
        "image_url": "https://images.unsplash.com/photo-1448375240586-882707db888b"
    },
    {
        "id": 3,
        "title": "Ocean Waves",
        "category": "Nature",
        "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
    },
    {
        "id": 4,
        "title": "Beautiful Lake",
        "category": "Nature",
        "image_url": "https://images.unsplash.com/photo-1439853949127-fa647821eba0"
    },
    {
        "id": 5,
        "title": "Desert Landscape",
        "category": "Nature",
        "image_url": "https://images.unsplash.com/photo-1509316785289-025f5b846b35"
    },
    {
        "id": 6,
        "title": "City Skyline",
        "category": "City",
        "image_url": "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df"
    },
    {
        "id": 7,
        "title": "Modern Building",
        "category": "Architecture",
        "image_url": "https://images.unsplash.com/photo-1487958449943-2429e8be8625"
    },
    {
        "id": 8,
        "title": "Night City",
        "category": "City",
        "image_url": "https://images.unsplash.com/photo-1519501025264-65ba15a82390"
    },
    {
        "id": 9,
        "title": "Coffee Cup",
        "category": "Food",
        "image_url": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085"
    },
    {
        "id": 10,
        "title": "Fresh Pizza",
        "category": "Food",
        "image_url": "https://images.unsplash.com/photo-1513104890138-7c749659a591"
    },
    {
        "id": 11,
        "title": "Burger",
        "category": "Food",
        "image_url": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd"
    },
    {
        "id": 12,
        "title": "Fresh Fruits",
        "category": "Food",
        "image_url": "https://images.unsplash.com/photo-1610832958506-aa56368176cf"
    },
    {
        "id": 13,
        "title": "Cute Dog",
        "category": "Animals",
        "image_url": "https://images.unsplash.com/photo-1552053831-71594a27632d"
    },
    {
        "id": 14,
        "title": "White Cat",
        "category": "Animals",
        "image_url": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba"
    },
    {
        "id": 15,
        "title": "Wild Elephant",
        "category": "Animals",
        "image_url": "https://images.unsplash.com/photo-1557050543-4d5f4e07ef46"
    },
    {
        "id": 16,
        "title": "Red Car",
        "category": "Cars",
        "image_url": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7"
    },
    {
        "id": 17,
        "title": "Sports Car",
        "category": "Cars",
        "image_url": "https://images.unsplash.com/photo-1503376780353-7e6692767b70"
    },
    {
        "id": 18,
        "title": "Laptop Workspace",
        "category": "Technology",
        "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853"
    },
    {
        "id": 19,
        "title": "Programming Laptop",
        "category": "Technology",
        "image_url": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4"
    },
    {
        "id": 20,
        "title": "Mobile Phone",
        "category": "Technology",
        "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9"
    }
]

const carousel_box = document.querySelector(".carousel_box")

image_data.map((val)=>{
    carousel_box.innerHTML+= `<img class = "carousel_image" src = "${val.image_url}" </img>`
})