// console.log("Hello World")

let updateBtns = document.getElementsByClassName('update-cart')


for (let i=0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        let productId= this.dataset.product
        let action = this.dataset.action
        console.log('productID:', productId, 'actioN:', action)

        console.log('USER: ', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        } else{
            console.log('1:User is logged in, sending data...')
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('2:User is logged in, sending data...')

    let url = '/update_item/'

    fetch( url, {
        method : 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload() // reloading each time is not efficient, we need to fix it.
    })
}
