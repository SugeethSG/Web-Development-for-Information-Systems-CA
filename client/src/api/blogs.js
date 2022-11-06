import blogs from "../data/blogs";

async function getBlogs() {
  let blogs2 = blogs;
  let username = localStorage.getItem("username");
  var response = await fetch('http://sugeethsg.pythonanywhere.com/GetBlogs', {
    method: "POST",
    body: JSON.stringify(
      {
        "username":username
      })
    });
    var result = await response.json();
    console.log({result});
    if (result.status == 200){
      let data = JSON.parse(result.data);
      blogs2 = data.blogs;
    }
    console.log({blogs2})
    return blogs2;
}

async function getBlog(id) {
  let blogs = await getBlogs();
  console.log({blogs})
  return blogs.filter((blog) => blog.id.toString() === id)[0];
}

async function deleteBlog(id) {
  let username = localStorage.getItem("username");
  console.log({id});
  var response = await fetch('http://sugeethsg.pythonanywhere.com/DeleteBlog', {
    method: "POST",
    body: JSON.stringify(
      {
        "username":username,
        "id": id
      })
    });
    var result = await response.json();
    console.log({result});
    if (result.status == 200){
      return true;
    }
		return false;
}

async function editBlog(blog) {
  let username = localStorage.getItem("username");
  console.log({blog});
  var response = await fetch('http://sugeethsg.pythonanywhere.com/UpdateBlog', {
    method: "POST",
    body: JSON.stringify(
      {
        "username":username,
        "id": blog.id,
        "title": blog.title,
        "img": blog.img,
        "content": blog.content
      })
    });
    var result = await response.json();
    console.log({result});
    if (result.status == 200){
      return true;
    }
		return false;
}

async function addBlog(blog) {
  let username = localStorage.getItem("username");
  console.log({blog});
  var response = await fetch('http://sugeethsg.pythonanywhere.com/AddBlog', {
    method: "POST",
    body: JSON.stringify(
      {
        "username":username,
        "title": blog.title,
        "img": blog.img,
        "content": blog.content
      })
    });
    var result = await response.json();
    console.log({result});
    if (result.status == 200){
      return true;
    }
		return false;
}

export { getBlogs, getBlog, deleteBlog, editBlog, addBlog };
