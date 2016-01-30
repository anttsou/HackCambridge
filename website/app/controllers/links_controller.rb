class LinksController < ApplicationController

  respond_to :html,:json,:xml
  
  def index

  end

  def show
    @link = Link.find(params[:id])
    respond_with @link
  end

  def new
    @link = Link.new
  end

  def edit
  end

  def create
    @link = Link.new(link_params)

    if @link.save
      # respond_with @event
      redirect_to @link, notice: 'Link was successfully submitted.'
    else
      render :new
    end
  end

  def update
  end

  def destroy
  end

  private
    # Only allow a trusted parameter "white list" through.
    def link_params
      params.require(:link).permit(:url)
    end
end
