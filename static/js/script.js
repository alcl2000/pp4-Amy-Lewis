$(document).ready(function(){
    $(".delete-cat").click(function(){
        return confirm('Are you sure you want to delete this category? All posts in this category will be deleted. This action cannot be undone')
    })
    $(".delete-post").click(function(){
        return confirm('Are you sure you want to delete this post? All comments on this post will also be deleted, this action cannot be undone')
    })
    $(".delete-comment").click(function(){
        return confirm('Are you sure you want to delete this comment? This action cannot be undone')
    })
    $(".delete-tag").click(function(){
        return confirm('Are you sure you want to delete this tag? This action cannot be undone')
    })
})